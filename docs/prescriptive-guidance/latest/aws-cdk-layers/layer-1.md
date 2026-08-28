---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-cdk-layers/layer-1.html
---

# Layer 1 constructs
<a name="layer-1"></a>

[L1 constructs](https://docs.aws.amazon.com/cdk/v2/guide/constructs.html#constructs_l1_using) are the building blocks of the AWS CDK and are easily distinguished from other constructs by the prefix  `Cfn`. For example, the Amazon DynamoDB package in the AWS CDK contains a `Table` construct, which is an L2 construct. The corresponding L1 construct is called `CfnTable`, and it directly represents a CloudFormation DynamoDB `Table`. It's impossible to use the AWS CDK without accessing this first layer, although an AWS CDK application typically never uses an L1 construct directly. However, in the majority of cases,  the L2 and L3 constructs that developers are accustomed to using rely heavily on L1 constructs. So you can think of L1 constructs as the bridge between CloudFormation and the AWS CDK.

The sole purpose of the AWS CDK is to generate CloudFormation templates by using standard coding languages. After you run the **cdk synth** CLI command and the resulting CloudFormation templates are generated, the AWS CDK's job is complete. The **cdk deploy** command is there just as a convenience, but what you're doing when you run that command happens entirely within CloudFormation. The piece of the puzzle that translates AWS CDK code into the format that CloudFormation understands is the L1 construct.

## The AWS CDK-CloudFormation lifecycle for L1 constructs
<a name="l1-lifecycle"></a>

The process for creating and using L1 constructs consists of these steps:

1. The AWS CDK build process converts CloudFormation specifications into programmatic code in the form of L1 constructs.

1. Developers write code that either directly or indirectly references L1 constructs as part of an AWS CDK application.

1. Developers run the **cdk synth** command to convert programmatic code back into the format dictated by the CloudFormation specifications (templates).

1. Developers run the **cdk deploy** command to deploy the CloudFormation stacks within these templates into AWS account environments.

Let's do a little exercise. Go to the [AWS CDK open source repository ](https://github.com/aws/aws-cdk)on GitHub, pick a random AWS service, and then go to the AWS CDK package for that service (located in `packages->aws-cdk-lib->aws-<servicename>->lib`). For this example let's pick Amazon S3, but this works for any service. If you look at the main [index.ts file](https://github.com/aws/aws-cdk/blob/main/packages/aws-cdk-lib/aws-s3/lib/index.ts) for that package, you'll see a line that reads:

```
export * from './s3.generated';
```

However, you won't see the `s3.generated` file anywhere in the corresponding directory. This is because L1 constructs are auto-generated from the [CloudFormation resource specification](https://docs.aws.amazon.com/en_en/AWSCloudFormation/latest/UserGuide/cfn-resource-specification.html) during the AWS CDK build process. So you'll see `s3.generated` in the package only after you run the AWS CDK build command for the package.

## The AWS CloudFormation resource specification
<a name="l1-spec"></a>

The AWS CloudFormation resource specification defines infrastructure as code (IAC) for AWS and determines how code within CloudFormation templates is converted into resources in an AWS account. This specification defines AWS resources in [JSON format](https://www.json.org/json-en.html) on a per-Region level. Each resource is given a unique [resource type name](https://docs.aws.amazon.com/en_en/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html) that follows the format `provider::service::resource`. For example, the resource type name for an Amazon S3 bucket would be `AWS::S3::Bucket`, and the resource type name for an Amazon S3 access point would be `AWS::S3::AccessPoint`. These resource types can be rendered in a CloudFormation template by using the syntax defined in the AWS CloudFormation resource specification. When the AWS CDK build process runs, each resource type also becomes an L1 construct.

Consequently, each L1 construct is a programmatic mirror image of its corresponding CloudFormation resource. Every property that you would apply in a CloudFormation template is available when you instantiate an L1 construct, and every required CloudFormation property is also required as an argument when you instantiate the corresponding L1 construct. The following table compares an S3 bucket as represented in a CloudFormation template with the same S3 bucket as defined as an AWS CDK L1 construct.

|
|
| CloudFormation template | L1 construct |
| --- |--- |
| <pre>"amzns3demobucket": {<br />    "Type": "AWS::S3::Bucket",<br />    "Properties": {<br />      "BucketName": "DOC-EXAMPLE-BUCKET",<br />      "BucketEncryption": {<br />        "ServerSideEncryptionConfiguration": [<br />          {<br />            "ServerSideEncryptionByDefault": {<br />              "SSEAlgorithm": "AES256"<br />            }<br />          }<br />        ]<br />      },<br />      "MetricsConfigurations": [<br />        {<br />          "Id": "myConfig"<br />        }<br />      ],<br />      "OwnershipControls": {<br />        "Rules": [<br />          {<br />            "ObjectOwnership": "BucketOwnerPreferred"<br />          }<br />        ]<br />      },<br />      "PublicAccessBlockConfiguration": {<br />        "BlockPublicAcls": true,<br />        "BlockPublicPolicy": true,<br />        "IgnorePublicAcls": true,<br />        "RestrictPublicBuckets": true<br />      },<br />      "VersioningConfiguration": {<br />        "Status": "Enabled"<br />      }<br />    }<br />  }</pre> | <pre>new CfnBucket(this, "amzns3demobucket", {<br />  bucketName: "DOC-EXAMPLE-BUCKET",<br />  bucketEncryption: {<br />    serverSideEncryptionConfiguration: [<br />      {<br />        serverSideEncryptionByDefault: {<br />          sseAlgorithm: "AES256"<br />        }<br />      }<br />    ]<br />  },<br />  metricsConfigurations: [<br />    {<br />      id: "myConfig"<br />    }<br />  ],<br />  ownershipControls: {<br />    rules: [<br />      {<br />        objectOwnership: "BucketOwnerPreferred"<br />      }<br />    ]<br />  },<br />  publicAccessBlockConfiguration: {<br />    blockPublicAcls: true,<br />    blockPublicPolicy: true,<br />    ignorePublicAcls: true,<br />    restrictPublicBuckets: true<br />  },<br />  versioningConfiguration: {<br />    status: "Enabled"<br />  }<br />});</pre> |

As you can see, the L1 construct is the exact manifestation in code of the CloudFormation resource. There are no shortcuts or simplifications, so the amount of boilerplate text that must be written is roughly the same. However, one of the great advantages to using the AWS CDK is supposed to be that it helps eliminate a lot of that boilerplate CloudFormation syntax. So how does that happen? That's where the L2 construct comes in.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
