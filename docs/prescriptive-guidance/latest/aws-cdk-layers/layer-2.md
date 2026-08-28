---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-cdk-layers/layer-2.html
---

# Layer 2 constructs
<a name="layer-2"></a>

The [AWS CDK open source repository](https://github.com/aws/aws-cdk) is written primarily by using the [TypeScript](https://www.typescriptlang.org/) programming language and consists of numerous packages and modules. The main package library, called `aws-cdk-lib`, is roughly divided into one package per AWS service, although this is not always the case. As previously discussed, the L1 constructs are automatically generated during the build process, so what is all that code you see when you look inside the repository? Those are [L2 constructs](https://docs.aws.amazon.com/cdk/v2/guide/constructs.html#constructs_using), which are abstractions of L1 constructs.

The packages also contain a collection of TypeScript types, enums, and interfaces as well as helper classes that add more functionality, but those items all serve L2 constructs. All L2 constructs call their corresponding L1 constructs in their constructors upon instantiation, and the resulting L1 construct that is created can be accessed from layer 2 like this:

```
const role = new Bucket(this, "DOC-EXAMPLE-BUCKET", {/*...BucketProps*/});
const cfnBucket = role.node.defaultChild;
```

The L2 construct takes the default properties, convenience methods, and other syntactic sugar and applies them to the L1 construct. This takes away much of the repetition and verbosity that is necessary to provision resources directly in CloudFormation.

All L2 constructs build their corresponding L1 constructs under the hood. However, L2 constructs don't actually extend L1 constructs. Both L1 and L2 constructs inherit a special class called [Construct](https://docs.aws.amazon.com/cdk/api/v2/docs/constructs.Construct.html). In version 1 of the AWS CDK the `Construct` class was built into the development kit, but in version 2 it's a separate [standalone package](https://www.npmjs.com/package/constructs). This is so other packages such as the [Cloud Development Kit for Terraform (CDKTF)](https://developer.hashicorp.com/terraform/cdktf) can include it as a dependency. Any class that inherits the `Construct` class is an L1, L2, or an L3 construct. L2 constructs extend this class directly while L1 constructs extend a class called `CfnResource`.

|
|
| **L1 inheritance tree** | **L2 inheritance tree** |
| --- |--- |
| *L1 construct*<br />*→ class *[*CfnResource*](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.CfnResource.html)<br />*→→ abstract class *[*CfnRefElement*](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.CfnRefElement.html)<br />*→→→ abstract class *[*CfnElement*](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.CfnElement.html)<br />*→→→→ class *[*Construct*](https://docs.aws.amazon.com/cdk/api/v2/docs/constructs.Construct.html) | *L2 construct*<br />*→ class *[*Construct*](https://docs.aws.amazon.com/cdk/api/v2/docs/constructs.Construct.html) |

If both L1 and L2 constructs inherit the `Construct` class, why don't L2 constructs just extend L1? Well, the classes between the `Construct` class and layer 1 lock the L1 construct in place as a mirror image of the CloudFormation resource. They contain abstract methods (methods that downstream classes *must* include) like `_toCloudFormation`, which forces the construct to directly output CloudFormation syntax. L2 constructs skip over those classes and extend the `Construct` class directly.  This gives them the flexibility to abstract much of the code needed for L1 constructs by building them separately within their constructors.

The previous section featured a side-by-side comparison of an S3 bucket from a CloudFormation template and that same S3 bucket rendered as an L1 construct. That comparison showed that the properties and syntax are nearly identical, and the L1 construct saves only three or four lines compared with the CloudFormation construct. Now let's compare the L1 construct with the L2 construct for the same S3 bucket:

|
|
| L1 construct for S3 bucket | L2 construct for S3 bucket |
| --- |--- |
| <pre>new CfnBucket(this, "amzns3demobucket", {<br />  bucketName: "DOC-EXAMPLE-BUCKET",<br />  bucketEncryption: {<br />    serverSideEncryptionConfiguration: [<br />      {<br />        serverSideEncryptionByDefault: {<br />          sseAlgorithm: "AES256"<br />        }<br />      }<br />    ]<br />  },<br />  metricsConfigurations: [<br />    {<br />      id: "myConfig"<br />    }<br />  ],<br />  ownershipControls: {<br />    rules: [<br />      {<br />        objectOwnership: "BucketOwnerPreferred"<br />      }<br />    ]<br />  },<br />  publicAccessBlockConfiguration: {<br />    blockPublicAcls: true,<br />    blockPublicPolicy: true,<br />    ignorePublicAcls: true,<br />    restrictPublicBuckets: true<br />  },<br />  versioningConfiguration: {<br />    status: "Enabled"<br />  }<br />});</pre> | <pre>new Bucket(this, "amzns3demobucket", {<br />  bucketName: "DOC-EXAMPLE-BUCKET",<br />  encryption: BucketEncryption.S3_MANAGED,<br />  metrics: [<br />    {<br />      id: "myConfig"<br />    },<br />  ],<br />  objectOwnership: ObjectOwnership.BUCKET_OWNER_PREFERRED,<br />  blockPublicAccess: BlockPublicAccess.BLOCK_ALL,<br />  versioned: true<br />});</pre> |

As you can see, the L2 construct is less than half the size of the L1 construct. L2 constructs use numerous techniques to accomplish this consolidation. Some of these techniques apply to a single L2 construct, but others can be reused across multiple constructs so they are separated into their own class for reusability. L2 constructs consolidate CloudFormation syntax in several ways, as discussed in the following sections.

## Default properties
<a name="l2-default-properties"></a>

The simplest way to consolidate the code for provisioning a resource is to turn the most common property settings into defaults. The AWS CDK has access to powerful programming languages and CloudFormation doesn't, so these defaults are often conditional in nature. Sometimes several lines of CloudFormation configuration can be eliminated from the AWS CDK code because those settings can be inferred from the values of other properties that are passed to the construct.

## Structs, types, and interfaces
<a name="l2-structs"></a>

Although the AWS CDK is available in several programming languages, it is written natively in TypeScript, so that language's type system is used to define the types that make up L2 constructs. Diving deep into that type system is beyond the scope of this guide; see the [TypeScript documentation](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html) for details. To summarize, a TypeScript type describes what kind of data a particular variable holds. This could be basic data such as a string, or more complex data such as an object. A TypeScript interface is another way of expressing the TypeScript object type, and a struct is another name for an interface.

TypeScript doesn't use the term *struct*, but if you look in the [AWS CDK API Reference](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-construct-library.html), you'll see that a struct is actually just another TypeScript interface within the code. The API Reference also refers to certain interfaces as interfaces, too. If structs and interfaces are the same thing, why does the AWS CDK documentation make a distinction between them?

What the AWS CDK refers to as structs are interfaces that represent any object used by an L2 construct. This includes the object types for the property arguments that are passed to the L2 construct during instantiation, like such as `BucketProps` for the S3 Bucket construct and `TableProps` for the DynamoDB Table construct, as well as other TypeScript interfaces that are used within the AWS CDK. In short, if it's a TypeSscript interface within the AWS CDK and it's name isn't prefixed by the letter `I`, the AWS CDK calls it a *struct*.

Conversely, the AWS CDK uses the term *interface* to represent the base elements a plain object would need to be considered a proper representation of a particular construct or helper class. That is, an interface describes what an L2 construct's public properties must be. All AWS CDK `interface` names are the names of existing constructs or helper classes prefixed by the letter `I`. All L2 constructs extend the `Construct` class, but they also implement their corresponding interface. So the L2 construct `Bucket` implements the `IBucket` interface.

## Static methods
<a name="l2-static-methods"></a>

Every instance of an L2 construct is also an instance of its corresponding interface, but the reverse isn't true. This is important when looking through a struct to see which data types are required. If a struct has a property called `bucket`, which requires the data type `IBucket`, you could pass either an object that contains the properties listed in the `IBucket` interface or an instance of an L2 `Bucket`. Either one would work. However, if that `bucket` property called for an L2 `Bucket`, you could pass only a `Bucket` instance in that field.

This distinction becomes very important when you import pre-existing resources into your stack. You can create an L2 construct for any resource that's native to your stack, but if you need to reference a resource that was created outside the stack, you have to use that L2 construct's interface. That's because creating an L2 construct creates a new resource if one doesn't already exist within that stack. References to existing resources must be plain objects that conform to that L2 construct's interface.

To make this easier in practice, most L2 constructs have a set of static methods associated with them that return that L2 construct's interface. These static methods usually start with the word `from`. The first two arguments passed to these methods are the same `scope` and `id` arguments required for a standard L2 construct. However, the third argument isn't `props` but a small subset of properties (or sometimes just one property) that defines an interface. For this reason, when you pass an L2 construct, only the elements of the interface are required in most cases. This is so, where possible, you can use imported resources as well.

```
// Example of referencing an external S3 bucket
const preExistingBucket = Bucket.fromBucketName(this, "external-bucket", "name-of-bucket-that-already-exists");
```

However, you shouldn't rely heavily on interfaces. You should import resources and use interfaces directly only when absolutely necessary, because interfaces don't provide many of the properties―such as helper methods―that make an L2 construct so powerful.

## Helper methods
<a name="l2-helper-methods"></a>

An L2 construct is a programmatic class rather than a simple object, so it can expose class methods that allow you to manipulate your resource configuration after instantiation has taken place. A good example of this is the AWS Identity and Access Management (IAM) L2 [Role](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_iam.Role.html) construct. The following snippets show two ways to create the same IAM role by using the L2 `Role` construct.

Without a helper method:

```
const role = new Role(this, "my-iam-role", {
   assumedBy: new FederatedPrincipal('my-identity-provider.com'),
   managedPolicies: [
      ManagedPolicy.fromAwsManagedPolicyName("ReadOnlyAccess")
   ],
   inlinePolicies: {
      lambdaPolicy: new PolicyDocument({
         statements: [
            new PolicyStatement({
               effect: Effect.ALLOW,
               actions: [ 'lambda:UpdateFunctionCode' ],
               resources: [ 'arn:aws:lambda:us-east-1:123456789012:function:my-function' ]
            })
         ]
      })
   }
});
```

With a helper method:

```
const role = new Role(this, "my-iam-role", {
   assumedBy: new FederatedPrincipal('my-identity-provider.com')
});

role.addManagedPolicy(ManagedPolicy.fromAwsManagedPolicyName("ReadOnlyAccess"));
role.attachInlinePolicy(new Policy(this, "lambda-policy", {
   policyName: "lambdaPolicy",
   statements: [
      new PolicyStatement({
         effect: Effect.ALLOW,
         actions: [ 'lambda:UpdateFunctionCode' ],
         resources: [ 'arn:aws:lambda:us-east-1:123456789012:function:my-function' ]
      })
   ]
 }));
```

The ability to use instance methods to manipulate resource configuration after instantiation gives L2 constructs a lot of additional flexibility over the previous layer. L1 constructs also inherit some resource methods (such as `addPropertyOverride`), but it's not until layer two that you get methods that are specifically designed for that resource and its properties.

## Enums
<a name="l2-enums"></a>

CloudFormation syntax often requires you to specify many details in order to provision a resource properly. However, the majority of use cases are often covered by only a handful of configurations. Representing those configurations by using a series of enumerated values can vastly reduce the amount of code needed.

For example, in the S3 bucket L2 code example from earlier in this section, you have to use the CloudFormation template's `bucketEncryption` property to provide all the details, including the name of the encryption algorithm to be used. Instead, the AWS CDK provides the `BucketEncryption` enum, which takes the five most common forms of bucket encryption and lets you express each by using single variable names.

What about the edge cases that aren't covered by the enums? One of the goals of an L2 construct is to simplify the task of provisioning a layer 1 resource, so certain edge cases that are less commonly used might not be supported in layer 2. To support these edge cases, the AWS CDK lets you manipulate the underlying CloudFormation resource properties directly by using the [addPropertyOverride](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.CfnResource.html#addwbrpropertywbroverridepropertypath-value) method. For more about property overrides, see the [Best practices](best-practices.md) section of this guide and the section[ Abstractions and escape hatches](https://docs.aws.amazon.com/cdk/v2/guide/cfn_layer.html) in the AWS CDK documentation.

## Helper classes
<a name="l2-helper-classes"></a>

Sometimes an enum can't accomplish the programmatic logic needed to configure a resource for a given use case. In these situations, the AWS CDK often offers a helper class instead. An enum is a simple object that offers a series of key-value pairs, whereas a helper class offers the full capabilities of a TypeScript class. A helper class can still act like an enum by exposing static properties, but those properties could then have their values internally set with conditional logic in the helper class constructor or in a helper method.

So although the `BucketEncryption` enum can reduce the amount of code needed to set an encryption algorithm on an S3 bucket, that same strategy would not work for setting time durations because there are simply too many possible values to choose from. Creating an enum for each value would be far more trouble than it's worth. For this reason, a helper class is used for an S3 bucket's default S3 Object Lock configuration settings, as represented by the [ObjectLockRetention](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.ObjectLockRetention.html) class. `ObjectLockRetention` contains two static methods: one for `compliance` retention and the other for `governance retention`. Both methods take an instance of the [Duration helper class ](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.Duration.html)as an argument to express the amount of time that the lock should be configured for.

Another example is the AWS Lambda helper class [Runtime](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_lambda.Runtime.html). At first glance, it might appear that the static properties associated with this class could be handled by an enum. However, under the hood, each property value represents an instance of the `Runtime` class itself, so the logic performed in the class's constructor could not be achieved within an enum.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
