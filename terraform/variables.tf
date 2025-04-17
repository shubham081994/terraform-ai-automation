# variables.tf
variable "resource_group_name" {
  description = "The name of the resource group"
  type        = string
}

variable "location" {
  description = "The Azure region where the resources will be deployed"
  type        = string
  default     = "East US"
}

variable "key_vault_name" {
  description = "The name of the Key Vault"
  type        = string
}
variable "sku_name" {
  default = "standard"
}