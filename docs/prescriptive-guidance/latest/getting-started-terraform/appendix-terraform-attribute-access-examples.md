---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/getting-started-terraform/appendix-terraform-attribute-access-examples.html
---

# Appendix: Terraform attribute access examples
<a name="appendix-terraform-attribute-access-examples"></a>

## Resource
<a name="appendix-resource"></a>

```
resource "aws_s3_bucket" "myS3Bucket" {
     bucket = "my-s3-bucket"
}

bucketName = aws_s3_bucket.myS3Bucket.bucket
```

## Data source
<a name="appendix-data-source"></a>

```
data "aws_s3_bucket" "myS3Bucket" {
     bucket = "my-s3-bucket"
}

bucketName = data.aws_s3_bucket.myS3Bucket.bucket
```

## Module
<a name="appendix-module"></a>

```
module "eks" {
    source = "terraform-aws-modules/eks/aws"
    version = "20.2.1"
}

vpc_id = module.eks.vpc_id
```

## Variable
<a name="appendix-variable"></a>

```
variable "my_variable" = {
   default = "dog"
}

animalType = var.my_variable
```

## Local
<a name="appendix-local"></a>

```
locals {
  type = "dog"
}

animalType = local.type
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
