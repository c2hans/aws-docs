---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/least-privilege-cloudformation/permissions-cloudformation-provisioned-resources.html
---

# Configuring least-privilege permissions for resources provisioned through CloudFormation
<a name="permissions-cloudformation-provisioned-resources"></a>

AWS CloudFormation allows you to provision many different types of AWS resources. Provisioned resources require their own set of permissions to function as intended and to configure who has access to those resources. The previous chapter reviewed options for configuring permissions to access and use the CloudFormation service. This chapter reviews how you can apply the principle of least privilege to resources provisioned through CloudFormation.

In this guide, it would be practically impossible to review the security recommendations and best practices for every type of AWS resource that can be provisioned through CloudFormation. If you have questions related to a specific service, we recommend that you review the documentation for that service. Most AWS service documents contain a security section and information about the permissions required to use that service. For a complete list of AWS service documentation, see [AWS Documentation](https://docs.aws.amazon.com/index.html).

The following are high-level, service-agnostic steps you can take to create CloudFormation templates that adhere to the principle of least privilege:

1. Prepare a list of resources that you are planning to provision by using CloudFormation.

1. See the [AWS Documentation](https://docs.aws.amazon.com/index.html) for the corresponding services and review the sections about security and access management. This helps you understand the service-specific requirements and recommendations.

1. Use the information you gathered in the previous steps to design CloudFormation templates and associated policies that allow only the required permissions and deny all others.

Next, this guide reviews an example of how you can apply the principle of least privilege in CloudFormation templates, using a real-world use case.

## Example: Amazon S3 bucket for storing pipeline artifacts
<a name="example-s3-bucket"></a>

This example creates an [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) bucket that is used to store [AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html) project artifacts. [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html) uses these stored artifacts. You can allow CodeBuild and CodePipeline to access this S3 bucket through service roles, and you control that access by using an Amazon S3 [bucket policy](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-policies.html). The following are the resource names used in this example:
+ `Deployfiles_build` is the name of the CodeBuild project.
+ `Deployment-Pipeline` is the name of the pipeline in CodePipeline.

### Define the Amazon S3 bucket
<a name="define-the-amazon-s3-bucket.f15c1eda-f8c6-523f-a422-80938ae0f316"></a>

First, you define the S3 bucket in the CloudFormation template, which is a YAML-formatted text file.

```
MySampleBucket:
  Type: AWS::S3::Bucket
  Properties:
    PublicAccessBlockConfiguration:
        BlockPublicAcls: true
        BlockPublicPolicy: true
        IgnorePublicAcls: true
        RestrictPublicBuckets: true
```

### Define the Amazon S3 bucket policy
<a name="define-the-amazon-s3-bucket-policy.2b240b40-4ded-5c47-980a-68197e931606"></a>

Next, in the CloudFormation template, you create a bucket policy that allows only the `Deployfiles_build` project and the `Deployment-Pipeline` pipeline to access the bucket.

```
MyBucketPolicy:
  Type: AWS::S3::BucketPolicy
  Properties:
    Bucket: !Ref MySampleBucket
    PolicyDocument:
      Version: "2012-10-17"
      Statement:
      - Sid: "S3ArtifactRepoAccess"
        Effect: Allow
        Action:
          - 's3:GetObject'
          - 's3:GetObjectVersion'
          - 's3:PutObject'
          - 's3:GetBucketVersioning'
        Resource:
          - !Sub 'arn:aws:s3:::${MySampleBucket}'
          - !Sub 'arn:aws:s3:::${MySampleBucket}/*'
        Principal:
          Service:
            - codebuild.amazonaws.com
            - codepipeline.amazonaws.com
        Condition:
          StringLike:
            'aws:SourceArn':
              - !Sub 'arn:aws:codebuild:${AWS::Region}:${AWS::AccountId}:project/Deployfiles_build'
              - !Sub 'arn:aws:codepipeline:${AWS::Region}:${AWS::AccountId}:Deployment-Pipeline'
              - !Sub 'arn:aws:codepipeline:${AWS::Region}:${AWS::AccountId}:Deployment-Pipeline/*'
```

Note the following about this bucket policy:
+ The `Resource` element lists two different types of resources that use the following Amazon Resource Name (ARN) formats:
  + The ARN format of an S3 object is `arn:$<Partition>:s3:::$<BucketName>/$<ObjectName>`.
  + The ARN format of an S3 bucket is `arn:$<Partition>:s3:::$<BucketName>`.

  `s3:GetObject`, `s3:GetObjectVersion`, and `s3:PutObject` require an S3 object resource type, and `s3:GetBucketVersioning `requires an S3 bucket resource type. For more information about the required resource types for each action, see [Actions, resources, and condition keys for Amazon S3](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazons3.html).
+ The `Principal` element lists the entities that are allowed to perform the Amazon S3 actions defined in the statement. In this case, only CodeBuild and CodePipeline are allowed to perform these actions.
+ The `Condition` element further restricts access to the S3 bucket so that only the `Deployfiles_build` CodeBuild project, the `Deployment-Pipeline` CodePipeline pipeline, and the pipeline actions can access the bucket.

### Create the service roles
<a name="create-the-service-roles.d14cdb5c-a4a1-5557-bb23-1271f2f122b7"></a>

Although the bucket policy controls access to the bucket, it doesn't grant permissions to CodeBuild and CodePipeline to access it. To grant access, you need to create a service role for each service and add the following statement to each. The services roles for CodeBuild and CodePipeline allow the services to access the S3 bucket and its objects.

```
Sid: "ViewAccessToS3ArtifactRepo"
Effect: Allow
Action:
  - 's3:GetObject'
  - 's3:GetObjectVersion'
  - 's3:PutObject'
  - 's3:GetBucketVersioning'
Resource:
  - !Sub 'arn:aws:s3:::${BuildArtifactsBucket}'
  - !Sub 'arn:aws:s3:::${BuildArtifactsBucket}/*'
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
