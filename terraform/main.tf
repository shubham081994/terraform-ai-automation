terraform {
  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
      #version = "4.26.0"
    }
  }
}

provider "azurerm" {
  features {}
  subscription_id = "3f98158e-d9e8-4576-be67-dec75da365d3"  # Add your Azure Subscription ID here
}


resource "azurerm_key_vault" "example" {
  name                        = var.key_vault_name
  location                    = var.location
  resource_group_name         = var.resource_group_name
  sku_name                    = var.sku_name
  tenant_id                   = data.azurerm_client_config.example.tenant_id
  soft_delete_retention_days  = 7
}

# If you want to use a Client Configuration:
data "azurerm_client_config" "example" {}
