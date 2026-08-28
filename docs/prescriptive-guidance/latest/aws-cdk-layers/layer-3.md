---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-cdk-layers/layer-3.html
---

# Layer 3 constructs
<a name="layer-3"></a>

If L1 constructs perform a literal translation of CloudFormation resources into programmatic code, and L2 constructs replace much of the verbose CloudFormation syntax with helper methods and custom logic, what do the [L3 constructs](https://docs.aws.amazon.com/cdk/v2/guide/constructs.html#constructs_lib) do? The answer to that is limited only by your imagination. You can create layer 3 to fit any specific use cases you find yourself in. If your project needs a resource that has a specific subset of properties, you can create a reusable L3 construct to meet that need.

L3 constructs are called *patterns* within the AWS CDK. A pattern is any object that extends the `Construct` class in the AWS CDK (or extends a class that extends the `Construct `class) to perform any abstracted logic beyond layer 2. When you use the AWS CDK CLI to run **cdk init** to start a new AWS CDK project, you must choose from three AWS CDK application types: `app`, `lib`, and `sample-app`.

![Instructions for Running cdk init](http://docs.aws.amazon.com/prescriptive-guidance/latest/aws-cdk-layers/images/guide-img/b3d19902-dcaf-4bb8-91d6-0ae9000416b5/images/ca08a7cf-f559-4ec4-bfb8-3d65a949059e.png)

`app` and `sample-app` both represent classic AWS CDK applications where you build and deploy CloudFormation stacks to AWS environments. When you choose `lib`, you're choosing to build a brand new L3 construct. `app` and `sample-app` allow you to pick any language that the AWS CDK supports, but you can only pick TypeScript with `lib`. This is because the AWS CDK is natively written in TypeScript and uses an open source system called [JSii](https://github.com/aws/jsii) to translate the original code into the other supported languages. When you choose `lib` to initiate your project, you're choosing to build an extension to the AWS CDK.

Any class that extends the `Construct` class can be an L3 construct, but the most common use cases for layer 3 are *resource interactions, resource extensions,* and* custom resources*. Most L3 constructs use one or more of these three cases in order to extend AWS CDK functionality.

## Resource interactions
<a name="l3-resource-interactions"></a>

A solution typically employs several AWS services that work together. For example, an Amazon CloudFront distribution often uses an S3 bucket as its origin and AWS WAF for protection against common exploits. An AWS AppSync API or Amazon API Gateway often uses Amazon DynamoDB tables as data sources for their APIs. A pipeline in AWS CodePipeline often uses Amazon S3 as its source and AWS CodeBuild for its build stages. In these cases it's often useful to create a single L3 construct that handles the provisioning of two or more interconnected L2 constructs.

Here's an example of an L3 construct that provisions a CloudFront distribution along with its S3 origin, an AWS WAF to put in front of it, an Amazon Route 53 record, and an AWS Certificate Manager (ACM) certificate to add a custom endpoint with encryption in transit― all in one reusable construct:

```
// Define the properties passed to the L3 construct
export interface CloudFrontWebsiteProps {
     distributionProps: DistributionProps
     bucketProps: BucketProps
     wafProps: CfnWebAclProps
     zone: IHostedZone
}

// Define the L3 construct
export class CloudFrontWebsite extends Construct {
     public distribution: Distribution

     constructor(
        scope: Construct,
        id: string,
        props: CloudFrontWebsiteProps
     ) {
         super(scope, id);

         const certificate = new Certificate(this, "Certificate", {
            domainName: props.zone.zoneName,
            validation: CertificateValidation.fromDns(props.zone)
         });
         const defaultBehavior = {
            origin: new S3Origin(new Bucket(this, "bucket", props.bucketProps))
         }
         const waf = new CfnWebACL(this, "waf", props.wafProps);
         this.distribution = new Distribution(this, id, {
            ...props.distributionProps,
            defaultBehavior,
            certificate,
            domainNames: [this.domainName],
            webAclId: waf.attrArn,
          });
     }
}
```

Notice that CloudFront, Amazon S3, Route 53, and ACM all use L2 constructs, but the web ACL (which defines rules for handling web requests) uses an L1 construct. This is because the AWS CDK is an evolving open source package that isn't fully complete, and there is no L2 construct for `WebAcl` yet. However, anyone can contribute to the AWS CDK by creating new L2 constructs. So until the AWS CDK offers an L2 construct for `WebAcl`, you have to use an L1 construct. To create a new website by using the L3 construct `CloudFrontWebsite`, you use the following code:

```
const siteADotCom = new CloudFrontWebsite(stack, "siteA", siteAProps);
const siteBDotCom = new CloudFrontWebsite(stack, "siteB", siteBProps);
const siteCDotCom = new CloudFrontWebsite(stack, "siteC", siteCProps);
```

In this example, the CloudFront `Distribution` L2 construct is exposed as a public property of the L3 construct. There will still be cases where you need to expose L3 properties such as this as necessary. In fact we're going to see `Distribution` again later, in the [Custom resources](#l3-custom-resources) section.

The AWS CDK includes a few examples of resource interaction patterns such as this one. In addition to the `aws-ecs` package that contains the L2 constructs for Amazon Elastic Container Service (Amazon ECS), the AWS CDK has a package called [aws-ecs-patterns](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ecs_patterns-readme.html). This package contains several L3 constructs that combine Amazon ECS with Application Load Balancers, Network Load Balancers, and target groups while offering different versions that are preset for Amazon Elastic Compute Cloud (Amazon EC2) and AWS Fargate. Because many serverless applications use Amazon ECS only with Fargate, these L3 constructs provide a convenience that can save developers time and customers money.

## Resource extensions
<a name="l3-resource-extensions"></a>

Some use cases require resources to have specific default settings that are not native to the L2 construct. At the stack level, this can be handled by using [aspects](https://docs.aws.amazon.com/cdk/v2/guide/aspects.html), but another convenient way to give an L2 construct new defaults is by extending layer 2. Because a construct is any class that inherits the `Construct` class, and L2 constructs extend that class, you can also create an L3 construct by directly extending an L2 construct.

This can be especially useful for custom business logic that supports a customer's singular needs. Let's suppose a company has a repository that stores all of its AWS Lambda function code in a single directory called `src/lambda` and that most Lambda functions reuse the same runtime and handler name each time. Instead of configuring the code path every time you configure a new Lambda function, you could create a new L3 construct:

```
export class MyCompanyLambdaFunction extends Function {
      constructor(
        scope: Construct,
        id: string,
        props: Partial<FunctionProps> = {}
     ) {
         super(scope, id, {
            handler: 'index.handler',
            runtime: Runtime.NODEJS_LATEST,
            code: Code.fromAsset(`src/lambda/${props.functionName || id}`),
            ...props
     });
}
```

You could then replace the L2 `Function` construct everywhere in the repository as follows:

```
new MyCompanyLambdaFunction(this, "MyFunction");
new MyCompanyLambdaFunction(this, "MyOtherFunction");
new MyCompanyLambdaFunction(this, "MyThirdFunction", {
   runtime: Runtime.PYTHON_3_11
});
```

The defaults allow you to create new Lambda functions on a single line, and the L3 construct is set up so you can still override the default properties if needed.

Extending L2 constructs directly works best when you just want to add new defaults to existing L2 constructs. If you need other custom logic as well, it's better to extend the `Construct` class. The reason for this stems from the `super` method, which is called within the constructor. In classes that extend other classes, the `super` method is used to call the parent class's constructor, and this **must** be the first thing that happens within your constructor. This means that any manipulation of passed arguments or other custom logic can happen only **after** the original L2 construct has been created. If you need to perform any of this custom logic before you instantiate your L2 construct, it's better to follow the pattern outlined previously in the [Resource interactions](#l3-resource-interactions) section.

## Custom resources
<a name="l3-custom-resources"></a>

[Custom resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-custom-resources.html) are a powerful feature in CloudFormation that allow you to run custom logic from a Lambda function that's activated during stack deployment. Whenever you need any processes during deployment that aren't directly supported by CloudFormation, you can use a custom resource to make it happen. The AWS CDK offers classes that allow you to create custom resources programmatically as well. By using custom resources within an L3 constructor, you can make a construct out of almost anything.

One of the advantages of using Amazon CloudFront is its strong global caching capabilities. If you want to manually reset that cache so that your website immediately reflects new changes made to your origin, you can use a [CloudFront invalidation](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Invalidation.html). However, invalidations are processes that run on** **a CloudFront distribution instead of being properties of a CloudFront distribution. They can be created and applied to an existing distribution at any time, so they aren't natively part of the provisioning and deployment process.

In this scenario, you might want to create and run an invalidation after every update to a distribution's origin. Because of custom resources, you can create an L3 construct that looks something like this:

```
export interface CloudFrontInvalidationProps {
     distribution: Distribution
     region?: string
     paths?: string[]
}

export class CloudFrontInvalidation extends Construct {
      constructor(
        scope: Construct,
        id: string,
        props: CloudFrontInvalidationProps
     ) {
          super(scope, id);
          const policy = AwsCustomResourcePolicy.fromSdkCalls({
               resources:AwsCustomResourcePolicy.ANY_RESOURCE
          });
          new AwsCustomResource(scope, `${id}Invalidation`, {
             policy,
             onUpdate: {
                  service: 'CloudFront',
                  action: 'createInvalidation',
                  region: props.region || 'us-east-1',
                  physicalResourceId: PhysicalResourceId.fromResponse('Invalidation.Id'),
                  parameters: {
                     DistributionId: props.distribution.distributionId,
                     InvalidationBatch: {
                         Paths: {
                            Quantity: props.paths?.length || 1,
                            Items: props.paths || ['/*']
                         },
                         CallerReference: crypto.randomBytes(5).toString('hex')
                     }
                  }
             }
          }
     }
}
```

Using the distribution we created earlier in the `CloudFrontWebsite` L3 construct, you could do this very easily:

```
new CloudFrontInvalidation(this, 'MyInvalidation', {
       distribution: siteADotCom.distribution
});
```

This L3 construct uses an AWS CDK L3 construct called [AwsCustomResource](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.custom_resources.AwsCustomResource.html) to create a custom resource that performs custom logic. `AwsCustomResource` is very convenient when you need to make exactly one AWS SDK call, because it allows you to do that without having to write any Lambda code. If you have more complex requirements and want to implement your own logic, you can use the basic [CustomResource](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.CustomResource.html) class directly.

Another good example of the AWS CDK using a custom resource L3 construct is** **[S3 bucket deployment](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3_deployment.BucketDeployment.html). The Lambda function created by the custom resource within the constructor of this L3 construct adds functionality that CloudFormation wouldn't be able to handle otherwise: it adds and updates objects in an S3 bucket. Without S3 bucket deployment, you wouldn't be able to put content into the S3 bucket you just created as part of your stack, which would be very inconvenient.

The best example of the AWS CDK eliminating the need to write out reams of CloudFormation syntax is this basic `S3BucketDeployment`:

```
new BucketDeployment(this, 'BucketObjects', {
  sources: [Source.asset('./DOC-EXAMPLE-BUCKET')],
  destinationBucket: amzns3demobucket
});
```

Compare that to the CloudFormation code that you'd have to write to accomplish the same thing:

```
 "lambdapolicyA5E98E09": {
   "Type": "AWS::IAM::Policy",
   "Properties": {
    "PolicyDocument": {
     "Statement": [
      {
       "Action": "lambda:UpdateFunctionCode",
       "Effect": "Allow",
       "Resource": "arn:aws:lambda:us-east-1:123456789012:function:my-function"
      }
     ],
     "Version": "2012-10-17"
    },
    "PolicyName": "lambdaPolicy",
    "Roles": [
     {
      "Ref": "myiamroleF09C7974"
     }
    ]
   },
   "Metadata": {
    "aws:cdk:path": "CdkScratchStack/lambda-policy/Resource"
   }
  },
  "BucketObjectsAwsCliLayer8C081206": {
   "Type": "AWS::Lambda::LayerVersion",
   "Properties": {
    "Content": {
     "S3Bucket": {
      "Fn::Sub": "cdk-hnb659fds-assets-${AWS::AccountId}-${AWS::Region}"
     },
     "S3Key": "e2277687077a2abf9ae1af1cc9565e6715e2ebb62f79ec53aa75a1af9298f642.zip"
    },
    "Description": "/opt/awscli/aws"
   },
   "Metadata": {
    "aws:cdk:path": "CdkScratchStack/BucketObjects/AwsCliLayer/Resource",
    "aws:asset:path": "asset.e2277687077a2abf9ae1af1cc9565e6715e2ebb62f79ec53aa75a1af9298f642.zip",
    "aws:asset:is-bundled": false,
    "aws:asset:property": "Content"
   }
  },
  "BucketObjectsCustomResourceB12E6837": {
   "Type": "Custom::CDKBucketDeployment",
   "Properties": {
    "ServiceToken": {
     "Fn::GetAtt": [
      "CustomCDKBucketDeployment8693BB64968944B69AAFB0CC9EB8756C81C01536",
      "Arn"
     ]
    },
    "SourceBucketNames": [
     {
      "Fn::Sub": "cdk-hnb659fds-assets-${AWS::AccountId}-${AWS::Region}"
     }
    ],
    "SourceObjectKeys": [
     "f888a9d977f0b5bdbc04a1f8f07520ede6e00d4051b9a6a250860a1700924f26.zip"
    ],
    "DestinationBucketName": {
     "Ref": "amzns3demobucket77F80CC0"
    },
    "Prune": true
   },
   "UpdateReplacePolicy": "Delete",
   "DeletionPolicy": "Delete",
   "Metadata": {
    "aws:cdk:path": "CdkScratchStack/BucketObjects/CustomResource/Default"
   }
  },
  "CustomCDKBucketDeployment8693BB64968944B69AAFB0CC9EB8756CServiceRole89A01265": {
   "Type": "AWS::IAM::Role",
   "Properties": {
    "AssumeRolePolicyDocument": {
     "Statement": [
      {
       "Action": "sts:AssumeRole",
       "Effect": "Allow",
       "Principal": {
        "Service": "lambda.amazonaws.com"
       }
      }
     ],
     "Version": "2012-10-17"
    },
    "ManagedPolicyArns": [
     {
      "Fn::Join": [
       "",
       [
        "arn:",
        {
         "Ref": "AWS::Partition"
        },
        ":iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
       ]
      ]
     }
    ]
   },
   "Metadata": {
    "aws:cdk:path": "CdkScratchStack/Custom::CDKBucketDeployment8693BB64968944B69AAFB0CC9EB8756C/ServiceRole/Resource"
   }
  },
  "CustomCDKBucketDeployment8693BB64968944B69AAFB0CC9EB8756CServiceRoleDefaultPolicy88902FDF": {
   "Type": "AWS::IAM::Policy",
   "Properties": {
    "PolicyDocument": {
     "Statement": [
      {
       "Action": [
        "s3:GetBucket*",
        "s3:GetObject*",
        "s3:List*"
       ],
       "Effect": "Allow",
       "Resource": [
        {
         "Fn::Join": [
          "",
          [
           "arn:",
           {
            "Ref": "AWS::Partition"
           },
           ":s3:::",
           {
            "Fn::Sub": "cdk-hnb659fds-assets-${AWS::AccountId}-${AWS::Region}"
           },
           "/*"
          ]
         ]
        },
        {
         "Fn::Join": [
          "",
          [
           "arn:",
           {
            "Ref": "AWS::Partition"
           },
           ":s3:::",
           {
            "Fn::Sub": "cdk-hnb659fds-assets-${AWS::AccountId}-${AWS::Region}"
           }
          ]
         ]
        }
       ]
      },
      {
       "Action": [
        "s3:Abort*",
        "s3:DeleteObject*",
        "s3:GetBucket*",
        "s3:GetObject*",
        "s3:List*",
        "s3:PutObject",
        "s3:PutObjectLegalHold",
        "s3:PutObjectRetention",
        "s3:PutObjectTagging",
        "s3:PutObjectVersionTagging"
       ],
       "Effect": "Allow",
       "Resource": [
        {
         "Fn::GetAtt": [
          "amzns3demobucket77F80CC0",
          "Arn"
         ]
        },
        {
         "Fn::Join": [
          "",
          [
           {
            "Fn::GetAtt": [
             "amzns3demobucket77F80CC0",
             "Arn"
            ]
           },
           "/*"
          ]
         ]
        }
       ]
      }
     ],
     "Version": "2012-10-17"
    },
    "PolicyName": "CustomCDKBucketDeployment8693BB64968944B69AAFB0CC9EB8756CServiceRoleDefaultPolicy88902FDF",
    "Roles": [
     {
      "Ref": "CustomCDKBucketDeployment8693BB64968944B69AAFB0CC9EB8756CServiceRole89A01265"
     }
    ]
   },
   "Metadata": {
    "aws:cdk:path": "CdkScratchStack/Custom::CDKBucketDeployment8693BB64968944B69AAFB0CC9EB8756C/ServiceRole/DefaultPolicy/Resource"
   }
  },
  "CustomCDKBucketDeployment8693BB64968944B69AAFB0CC9EB8756C81C01536": {
   "Type": "AWS::Lambda::Function",
   "Properties": {
    "Code": {
     "S3Bucket": {
      "Fn::Sub": "cdk-hnb659fds-assets-${AWS::AccountId}-${AWS::Region}"
     },
     "S3Key": "9eb41a5505d37607ac419321497a4f8c21cf0ee1f9b4a6b29aa04301aea5c7fd.zip"
    },
    "Role": {
     "Fn::GetAtt": [
      "CustomCDKBucketDeployment8693BB64968944B69AAFB0CC9EB8756CServiceRole89A01265",
      "Arn"
     ]
    },
    "Environment": {
     "Variables": {
      "AWS_CA_BUNDLE": "/etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem"
     }
    },
    "Handler": "index.handler",
    "Layers": [
     {
      "Ref": "BucketObjectsAwsCliLayer8C081206"
     }
    ],
    "Runtime": "python3.9",
    "Timeout": 900
   },
   "DependsOn": [
  "CustomCDKBucketDeployment8693BB64968944B69AAFB0CC9EB8756CServiceRoleDefaultPolicy88902FDF",
    "CustomCDKBucketDeployment8693BB64968944B69AAFB0CC9EB8756CServiceRole89A01265"
   ],
   "Metadata": {
    "aws:cdk:path": "CdkScratchStack/Custom::CDKBucketDeployment8693BB64968944B69AAFB0CC9EB8756C/Resource",
    "aws:asset:path": "asset.9eb41a5505d37607ac419321497a4f8c21cf0ee1f9b4a6b29aa04301aea5c7fd",
    "aws:asset:is-bundled": false,
    "aws:asset:property": "Code"
   }
  }
```

4 lines versus 241 lines is a **huge** difference\! And this is just one example of what's possible when you leverage layer 3 to customize your stacks.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
