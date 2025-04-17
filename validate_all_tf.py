import os
import datetime
from openai import AzureOpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT")

# Create OpenAI client
client = AzureOpenAI(
    api_key=AZURE_OPENAI_KEY,
    api_version="2023-05-15",
    azure_endpoint=AZURE_OPENAI_ENDPOINT
)

def analyze_terraform_code(code):
    system_prompt = (
        "You are an expert DevOps and Cloud engineer. "
        "Analyze the given Terraform code for security issues, best practices, and optimization improvements. "
        "Provide a list of issues and suggestions categorized under Security, Best Practices, and Optimization."
    )

    try:
        response = client.chat.completions.create(
            model=AZURE_OPENAI_DEPLOYMENT,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": code}
            ],
            temperature=0.3,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error during analysis: \n\n{e}"

def validate_terraform(terraform_folder="terraform"):
    tf_files = []
    for root, _, files in os.walk(terraform_folder):
        for file in files:
            if file.endswith(".tf"):
                with open(os.path.join(root, file), 'r') as f:
                    tf_files.append(f.read())

    if not tf_files:
        print("No Terraform files found.")
        return

    all_code = "\n\n".join(tf_files)
    analysis = analyze_terraform_code(all_code)

    # Estimate issue percentage
    lines_total = len(all_code.splitlines())
    issues_total = analysis.count("- ")
    percentage_flagged = (issues_total / lines_total) * 100 if lines_total > 0 else 100
    status_symbol = lambda x: "✅" if x < 15 else "❌"

    security_status = status_symbol(percentage_flagged)
    best_practice_status = status_symbol(percentage_flagged)
    optimization_status = status_symbol(percentage_flagged)

    # Ensure reports/ directory exists
    report_dir = "reports"
    os.makedirs(report_dir, exist_ok=True)

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_filename = os.path.join(report_dir, f"validation_report_{timestamp}.md")

    with open(report_filename, "w") as report:
        report.write("# Terraform Validation Report\n\n")
        report.write(f"**Generated:** {timestamp}\n\n")
        report.write("## Summary\n\n")
        report.write("| Check           | Status   |\n")
        report.write("|----------------|----------|\n")
        report.write(f"| Security       | {security_status} |\n")
        report.write(f"| Best Practices | {best_practice_status} |\n")
        report.write(f"| Optimization   | {optimization_status} |\n")
        report.write("\n## Details\n\n")
        report.write(analysis)

    print(f"✅ Validation complete. Report saved to **{report_filename}**")

if __name__ == "__main__":
    validate_terraform("terraform")
