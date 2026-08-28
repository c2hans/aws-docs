---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/getting-started-terraform/functions-expressions.html
---

# Functions, expressions, and meta-arguments
<a name="functions-expressions"></a>

One criticism of IaC tools that use declarative configuration files rather than common programming languages is that they make it more difficult to implement custom programmatic logic. In Terraform configurations, this issue is addressed by using functions, expressions, and meta-arguments.

## Functions
<a name="functions"></a>

One of the great advantages to using code to provision your infrastructure is the ability to store common workflows  and reuse them again and again, often passing different arguments each time. Terraform functions are similar to AWS CloudFormation [intrinsic functions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference.html), although their syntax is more similar to how functions are called in programmatic languages. You might have already noticed some Terraform functions, such as like [substr](https://developer.hashicorp.com/terraform/language/functions/substr), [concat](https://developer.hashicorp.com/terraform/language/functions/concat),[length](https://developer.hashicorp.com/terraform/language/functions/length), and [base64decode](https://developer.hashicorp.com/terraform/language/functions/base64decode), in the examples in this guide. Like CloudFormation with intrinsic functions, Terraform has a series of [built-in functions](https://developer.hashicorp.com/terraform/language/functions) that are available for use in your configurations. For example, if a particular resource attribute takes a very large JSON object that would be inefficient to paste directly into the file, you could put the object in a **.json** file and use Terraform functions to access it. In the following example, the `file` function returns the contents of the file in string form, and then the `jsondecode` function converts it into an object type.

```
resource "example_resource" "example_resource_name" {
  json_object = jsondecode(file("/path/to/file.json"))
}
```

## Expressions
<a name="expressions"></a>

Terraform also allows for [conditional expressions](https://developer.hashicorp.com/terraform/language/expressions/conditionals), which are similar to CloudFormation `condition` functions except that they use the more traditional [ternary operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_operator) syntax. In the following example, the two expressions return the exact same result. The second example is what Terraform calls a [splat expression](https://developer.hashicorp.com/terraform/language/expressions/splat). The asterisk causes Terraform to loop through the list and create a new list by using just the `id` property of each item.

```
resource "example_resource" "example_resource_name" {
  boolean_value  = var.value ? true : false
  numeric_value  = var.value > 0 ? 1 : 0
  string_value   = var.value == "change_me" ? "New value" : var.value
  string_value_2 = var.value != "change_me" ? var.value : "New value"
}
There are two ways to express for loops in a Terraform configuration:
resource "example_resource" "example_resource_name" {
  list_value   = [for object in var.ids : object.id]
  list_value_2 = var.ids[*].id
}
```

## Meta-arguments
<a name="meta-arguments"></a>

In the previous code example, `list_value` and `list_value_2` are referred to as *arguments*. You might be familiar with some of these meta-arguments already. Terraform also has a few *meta-arguments*, which act just like arguments but with some extra functionality:
+ The [depends\_on](https://developer.hashicorp.com/terraform/language/meta-arguments/depends_on) meta-argument is very similar to the CloudFormation [DependsOn attribute](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-dependson.html).
+ The [provider](https://developer.hashicorp.com/terraform/language/meta-arguments#provider) meta-argument allows you to use multiple provider configurations at once.
+ The [lifecycle ](https://developer.hashicorp.com/terraform/language/meta-arguments/lifecycle)meta-argument allows you to customize resource settings, similar to [removal](https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk/RemovalPolicy.html) and [deletion](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-deletionpolicy.html) policies in CloudFormation.

Other meta-arguments allow for function and expression functionality to be added directly to a resource. For example, the [count](https://developer.hashicorp.com/terraform/language/meta-arguments/count) meta-argument is a useful mechanism to create multiple similar resources at the same time. The following example demonstrates how to create two Amazon Elastic Container Service (Amazon EKS) clusters without using the `count` meta-argument.

```
resource "aws_eks_cluster" "example_0" {
  name     = "example_0"
  role_arn = aws_iam_role.cluster_role.arn
  vpc_config {
    endpoint_private_access = true
    endpoint_public_access  = true
    subnet_ids              = var.subnet_ids[0]
  }
}

resource "aws_eks_cluster" "example_1" {
  name     = "example_1"
  role_arn = aws_iam_role.cluster_role.arn
  vpc_config {
    endpoint_private_access = true
    endpoint_public_access  = true
    subnet_ids              = var.subnet_ids[1]
  }
}
```

The following example demonstrates how to use the `count` meta-argument to create two Amazon EKS clusters.

```
resource "aws_eks_cluster" "clusters" {
  count    = 2
  name     = "cluster_${count.index}"
  role_arn = aws_iam_role.cluster_role.arn
  vpc_config {
    endpoint_private_access = true
    endpoint_public_access  = true
    subnet_ids              = var.subnet_ids[count.index]
  }
}
```

To give each a unit name, you can access the list index within the resource block at `count.index`. But what if you want to create multiple similar resources that are a little more complex? That's where the [for\_each](https://developer.hashicorp.com/terraform/language/meta-arguments/for_each) meta-argument comes in. The `for_each` meta-argument is very similar to `count`, except that you pass in a list or an object instead of a number. Terraform creates a new resource for each member of the list or object. It is similar to if you set `count = length(list)`, except you can access the contents of the list rather than the loop index.

This works for both a list of items or a single object. The following example would create two resources that have `id-0` and `id-1` as their IDs.

```
variable "ids" {
  default = [
    { id = "id-0" },
    { id = "id-1" },
  ]
}

resource "example_resource" "example_resource_name" {
  # If your list fails, you might have to call "toset" on it to convert it to a set
  for_each = toset(var.ids)
  id       = each.value
}
```

The following example would create two resources as well, one for Sparky, the poodle, and one for Fluffy, the chihuahua.

```
variable "dogs" {
  default = {
    poodle    = "Sparky"
    chihuahua = "Fluffy"
  }
}

resource "example_resource" "example_resource_name" {
  for_each = var.dogs
  breed    = each.key
  name     = each.value
}
```

Just like you can access the loop index in count by using count.index, you can access the key and the value of each item in a for\_each loop by using the each object. Because for\_each iterates over both lists and objects, the each key and value can get a little confusing to keep track of. The following table shows the different ways that you can use the for\_each meta-argument and how you can reference the values upon each iteration.

|
|
| Example | `for_each` type | First iteration | Second iteration |
| --- |--- |--- |--- |
| **A** | <pre>["poodle", "chihuahua"]</pre> | <pre>each.key = "poodle"<br /><br />each.value = null</pre> | <pre>each.key = "chihuahua"<br /><br />each.value = null</pre> |
| **B** | <pre>[<br /><br />{<br /><br />type = "poodle",<br /><br />name = "Sparky"<br /><br />},<br /><br />{<br /><br />type = "chihuahua",<br /><br />name = "Fluffy"<br /><br />}<br /><br />]</pre> | <pre>each.key = {<br /><br />type = "poodle",<br /><br />name = "Sparky"<br /><br />}<br /><br />each.value = null</pre> | <pre>each.key = {<br /><br />type = "chihuahua",<br /><br />name = "Fluffy"<br /><br />}<br /><br />each.value = null</pre> |
| **C** | <pre>{<br /><br />poodle = "Sparky",<br /><br />chihuahua = "Fluffy"<br /><br />}</pre> | <pre>each.key = "poodle"<br /><br />each.value = "Sparky"</pre> | <pre>each.key = "chihuahua"<br /><br />each.value = "Fluffy"</pre> |
| **D** | <pre>{<br /><br />dogs = {<br /><br />poodle = "Sparky",<br /><br />chihuahua = "Fluffy"<br /><br />},<br /><br />cats = {<br /><br />persian = "Felix",<br /><br />burmese = "Morris"<br /><br />}<br /><br />}</pre> | <pre>each.key = "dogs"<br /><br />each.value = {<br /><br />poodle = "Sparky",<br /><br />chihuahua = "Fluffy"<br /><br />}</pre> | <pre>each.key = "cats"<br /><br />each.value = {<br /><br />persian = "Felix",<br /><br />burmese = "Morris"<br /><br />}</pre> |
| **E** | <pre>{<br /><br />dogs = [<br /><br />{<br /><br />type = "poodle",<br /><br />name = "Sparky"<br /><br />},<br /><br />{<br /><br />type = "chihuahua",<br /><br />name = "Fluffy"<br /><br />}<br /><br />],<br /><br />cats = [<br /><br />{<br /><br />type = "persian",<br /><br />name = "Felix"<br /><br />},<br /><br />{<br /><br />type = "burmese",<br /><br />name = "Morris"<br /><br />}<br /><br />]<br /><br />}</pre> | <pre>each.key = "dogs"<br /><br />each.value = [<br /><br />{<br /><br />type = "poodle",<br /><br />name = "Sparky"<br /><br />},<br /><br />{<br /><br />type = "chihuahua",<br /><br />name = "Fluffy"<br /><br />}<br /><br />]</pre> | <pre>each.key = "cats"<br /><br />each.value = [<br /><br />{<br /><br />type = "persian",<br /><br />name = "Felix"<br /><br />},<br /><br />{<br /><br />type = "burmese",<br /><br />name = "Morris"<br /><br />}<br /><br />]</pre> |

So if `var.animals` was equal to row E, then you could create one resource per animal by using the following code.

```
resource "example_resource" "example_resource_name" {
  for_each = var.animals
  type     = each.key
  breeds   = each.value[*].type
  names    = each.value[*].name
}
```

Alternatively, you could create two resources per animal by using the following code.

```
resource "example_resource" "example_resource_name" {
  for_each = var.animals.dogs
  type     = "dogs"
  breeds   = each.value.type
  names    = each.value.name
}

resource "example_resource" "example_resource_name" {
  for_each = var.animals.cats
  type     = "cats"
  breeds   = each.value.type
  names    = each.value.name
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
