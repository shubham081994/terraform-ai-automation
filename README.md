
# 🚀 AI-Powered Terraform Validation with Azure OpenAI & Azure DevOps

**Validate your Terraform Infrastructure-as-Code (IaC) using Azure OpenAI and integrate it seamlessly into your Azure DevOps CI/CD pipeline.**

---

## 📌 Overview

Terraform simplifies infrastructure provisioning, but ensuring code quality, security, and best practices can be time-consuming. This AI-powered assistant leverages **Azure OpenAI** to automate Terraform validation and generate insightful reports—making your DevOps process smarter and more efficient.

---

## ✅ Features

- 🔐 **Security Checks** – Detect hardcoded secrets, missing access policies, and insecure configurations.
- 🛠️ **Best Practices** – Validate naming, version pinning, modularity, and code structure.
- 🚀 **Optimization Insights** – Identify ways to improve performance and maintainability.
- 📄 **Markdown Reports** – Auto-generated summaries for every validation.
- 🔄 **CI/CD Integration** – Works out-of-the-box with Azure DevOps Pipelines.

---

## ⚙️ Prerequisites

- Python 3.8+
- Azure OpenAI resource and deployment
- `openai>=1.0.0`
- Terraform `.tf` files in a folder (e.g., `terraform/`)

Install requirements:

```bash
pip install -r requirements.txt
```

---

## 🗂️ Project Structure

```
.
├── terraform/                # Your Terraform configurations
├── reports/                 # Generated validation reports
├── validate_all_tf.py       # AI-powered validation script
├── azure-pipelines.yml      # Azure DevOps CI/CD pipeline
```

---

## 🧠 How It Works

- Aggregates all Terraform files
- Sends the code to Azure OpenAI
- Analyzes for security, optimization, and best practices
- Creates a summary report with ✅/❌ checks and suggestions

---

## 🖥️ Running Validation Locally

```bash
python validate_all_tf.py
```

The report will be saved to the `reports/` folder as a `.md` file.

---

## 🔁 Azure DevOps Integration

1. Create a [Variable Group](https://learn.microsoft.com/en-us/azure/devops/pipelines/library/variable-groups) in Azure DevOps:
   - `AZURE_OPENAI_KEY` (secret)
   - `AZURE_OPENAI_ENDPOINT`
   - `AZURE_OPENAI_DEPLOYMENT`

2. Use the provided `azure-pipelines.yml` to automate:
   - Python environment setup
   - Dependency installation
   - Terraform validation
   - Report artifact upload

Example pipeline steps:

```yaml
- script: |
    python validate_all_tf.py
  displayName: 'Run Terraform Validation'
```

---

## 📊 Example Output

Sample validation report structure:

```markdown
# Terraform Validation Report

**Generated:** 2025-04-17_07-25-04

## Summary

| Check           | Status   |
|----------------|----------|
| Security       | ✅ |
| Best Practices | ✅ |
| Optimization   | ✅ |

## Details

- Hardcoded subscription IDs
- Unpinned provider versions
- Lack of access policies
```

---

## 💡 Benefits

- Automates security and quality checks during every PR
- Reduces manual code reviews
- Improves consistency across teams
- Produces clear documentation artifacts

---

## 🔮 Future Enhancements

- Slack/Teams alerts for failed validations
- GitHub PR comment bot
- Support for other IaC tools: Bicep, ARM, CloudFormation
- Custom policy configuration

---

## 🧠 Conclusion

This AI assistant brings intelligence to your DevOps workflow. By combining Terraform with Azure OpenAI, you gain smarter reviews, cleaner code, and more secure infrastructure—all automatically.
