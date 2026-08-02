---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/getting-started-terraform/data-sources.html
---

# Data sources
<a name="data-sources"></a>

It's very common for deployment stacks to rely on data from previously existing resources. Most IaC tools have a way of importing resources that were created by some other process. These imported resources are usually read only (although [IAM roles](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_iam.IRole.html#attachwbrinlinewbrpolicypolicy) are a notable exception) and are used to access data needed by resources within the stack. AWS CloudFormation allows for importing resources, but this idea can be better explained by looking at the AWS Cloud Development Kit (AWS CDK).

The AWS CDK helps developers use existing programming languages to generate CloudFormation templates. The end result of an AWS CDK operation is an imported resource in CloudFormation. However the syntax used with the AWS CDK makes for an easier comparison with Terraform. Here's an example of importing a resource by using the AWS CDK.

```
const importedBucket: IBucket = Bucket.fromBucketAttributes(
    scope,
    "imported-bucket",
    {
        bucketName: "My_S3_Bucket"
    }
);
```

An imported resource is usually created by calling a static method on the same class you use to create a new resource of the same kind. Calling `new Bucket(...` would create a new resource, and calling `Bucket.fromBucketAttributes(...` imports an existing one. You pass a subset of the bucket's properties into the function so the AWS CDK can find the right bucket. Another difference, however, is that creating a new bucket returns a full instance of the `Bucket` class, with all properties and methods available within. Importing the resource returns an `IBucket`, which is a type that contains only the properties that `Bucket` must have. Although you can import a resource from an external stack, the options of what you can do with it are limited.

In Terraform, a similar goal is accomplished by using [data sources](https://developer.hashicorp.com/terraform/language/data-sources). Most defined Terraform resources have an accompanying data source available alongside it. The following is an example of a Terraform S3 bucket resource followed by its corresponding data source.

```
# S3 Bucket resource:
resource "aws_s3_bucket" "My_S3_Bucket" {
  bucket = "My_S3_Bucket"
}

# S3 Bucket data source:
data "aws_s3_bucket" "My_S3_Bucket" {
  bucket = "My_S3_Bucket"
}
```

The only difference between these two items is the name prefix. As shown in the [documentation](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/s3_bucket) for a data source, there are fewer parameters available that you can pass to a data source than a resource. This is because the resource uses those parameters to declare all of the properties of a new Amazon S3 bucket, while the data source needs just enough information to uniquely identify and import the data of an existing resource.

The similarity between the syntax of a Terraform resource and a data source can be convenient, but it can also be problematic. It's common for novice Terraform developers to accidentally used a data source rather than a resource in their configuration. Terraform data sources are always read only. You can use them in place of the corresponding resource for read actions (such as supplying an ID name to another resource). However, you can't use them for write actions, which fundamentally change some aspect of the underlying resource. For this reason, you can think of a Terraform data source as a cloned version of the underlying resource.

Similar to the previous AWS CDK IBucket example, data sources are useful for read-only scenarios. If you need to get data from an existing resource but don't need to maintain that resource within your stack, use a data source. A good example of this is when you're creating an Amazon EC2 instance that uses the account's default VPC. Because that VPC already exists, all you need to do is pull in its data. The following code sample shows how to use data to identify the target VPC.

```
data "aws_vpc" "default" {
  default = true
}

resource "aws_instance" "instance1" {
  ami           = "ami-123456"
  instance_type = "t2.micro"
  subnet_id     = data.aws_vpc.default.main_route_table_id
}
```
