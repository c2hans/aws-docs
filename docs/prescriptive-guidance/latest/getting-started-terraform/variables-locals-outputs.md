---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/getting-started-terraform/variables-locals-outputs.html
---

# Variables, local values, and outputs
<a name="variables-locals-outputs"></a>

Variables enhance code flexibility by allowing for placeholders within blocks of code. Variables can represent different values whenever the code is reused. Terraform distinguishes between its variable types by their modular scope. Input variables are external values that can be injected into a module, output values are internal values that can be shared externally, and local values always stay within their original scope.

## Variables
<a name="variables"></a>

AWS CloudFormation uses [parameters](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html) to represent custom values that can be set and reset from one stack deployment to the next. Similarly, Terraform uses [input variables](https://developer.hashicorp.com/terraform/language/values/variables), or *variables*. Variables can be declared anywhere in a Terraform configuration file and are usually declared with the required data type or default value. All three of the following expressions are valid Terraform variable declarations.

```
variable "thing_i_made_up" {
  type = string
}

variable "random_number" {
  default = 5
}

variable "dogs" {
  type = list(object({
    name  = string
    breed = string
  }))

  default = [
    {
      name  = "Sparky",
      breed = "poodle"
    }
  ]
}
```

To access Sparky's breed within the configuration, you'd use the variable `var.dogs[0].breed`. If a variable has no default and is not classified as nullable, then the value of the variable must be set for each deployment. Otherwise, it's optional to set a new value for the variable. In a root module, you can set current variable values on the [command line](https://developer.hashicorp.com/terraform/language/values/variables#variables-on-the-command-line), as [environment variables](https://developer.hashicorp.com/terraform/language/values/variables#environment-variables), or in the [terraform.tfvars](https://developer.hashicorp.com/terraform/language/values/variables#variable-definitions-tfvars-files) file. The following example shows how to enter variable values in the **terraform.tfvars** file, which is stored in the module's top-level directory.

```
# terraform.tfvars
dogs = [
   {
      name  = "Sparky",
      breed = "poodle"
   },
   {
      name  = "Fluffy",
      breed = "chihuahua"
   }
]

random_number = 7

thing_i_made_up = "Kabibble"
```

The value for `dogs` in this example **terraform.tfvars** file would override the default value in the variable declaration. If you're declaring variables within a child module, you can set the variable values directly within the module declaration block, as shown in the following example.

```
module "my_custom_module" {
  source        = "modulesource/custom"
  version       = "0.0.1"
  random_number = 8
}
```

Some of the other arguments you can use when declaring a variable include:
+ `sensitive` – Setting this to `true` prevents the variable value from being exposed in Terraform process outputs.
+ `nullable` – Setting this to `true` allows the variable to have no value. This is convenient for variables where a default is not set.
+ `description` – Add a description of the variable to the metadata for the stack.
+ `validation` – Set validation rules for the variable.

One of the most convenient aspects of Terraform variables is the ability to add one or more validation objects  within the variable declaration. You can use validation objects to add a condition that the variable must pass or else the deployment fails. You can also set a custom error message to show whenever the condition is violated.

For example, you're setting up a Terraform configuration file that members of your team will run. Before deploying the stacks, a team member needs to create a **terraform.tfvars** file to set an important configuration value. To remind them, you could do something like the following.

```
variable "important_config_setting" {
  type = string

  validation {
    condition     = length(var.important_config_setting) > 0
    error_message = "Don't forget to create the terraform.tfvars file!"
  }

  validation {
    condition     = substr(var.important_config_setting, 0, 7) == "prefix-"
    error_message = "Remember that the value always needs to start with 'prefix-'"
  }
}
```

As shown in this example, you can set multiple conditions inside a single variable. Terraform only shows error messages for failed conditions. In this way, you can enforce all kinds of rules on variable values. If a variable value causes a pipeline failure, you would know exactly why.

## Local values
<a name="local-values"></a>

If there are any values within a module that you'd like to alias, use the `locals` keyword rather than declaring a default variable that will never be updated. As the name suggests, a `locals` block contains terms that are scoped internally to that specific module. If you want to transform a string value, such as by adding a prefix to a variable value for use in a resource name, using a local value might be a good solution. A single `locals` block can declare all local values for your module, as shown in the following example.

```
locals {
  moduleName    = "My Module"
  localConfigId = concat("prefix-", var.important_config_setting)
}
```

Just remember that when you're accessing the value, the `locals` keyword becomes singular, such as `local.LocalConfigId`.

## Output values
<a name="output-values"></a>

If Terraform input variables are like CloudFormation parameters, then you could say that [Terraform output values ](https://developer.hashicorp.com/terraform/language/values/outputs)are like [CloudFormation outputs](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/outputs-section-structure.html). Both are used to expose values from within a deployment stack. However, because the Terraform module is more ingrained into the fabric of the tool, Terraform output values are also used to expose values within a module to a parent module or other child modules, even if those modules are all within the same deployment stack. If you're building two custom modules and the first module needs to access the ID value of the second module, then you'll need to add the following `output` block to the second module.

```
output "module_id" {
  value = local.module_id
}
Then in the first module you could use it like this:
module "first_module" {
  source = "path/to/first/module"
}

resource "example_resource" "example_resource_name" {
  module_id = module.first_module.module_id
}
```

Because Terraform output values can be used within the same stack, you can also use the `sensitive` attribute in an `output` block to suppress the value from being displayed in the stack output. Additionally, an `output` block can use `precondition` blocks in the same way that variables use `validation` blocks: to ensure variables follow a certain set of rules. This helps make sure that all values within a module exist as expected before proceeding with deployment.

```
output "important_config_setting" {
  value = var.important_config_setting

  precondition {
    condition     = length(var.important_config_setting) > 0
    error_message = "You forgot to create the terraform.tfvars file again."
  }
}
```
