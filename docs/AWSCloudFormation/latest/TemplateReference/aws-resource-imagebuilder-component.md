---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-imagebuilder-component.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ImageBuilder::Component
<a name="aws-resource-imagebuilder-component"></a>

Creates a new component that can be used to build, validate, test, and assess your image. The component is based on a YAML document that you specify using exactly one of the following methods:
+ Inline, using the `data` property in the request body.
+ A URL that points to a YAML document file stored in Amazon S3, using the `uri` property in the request body.

Image Builder determines the component type from the document. If the document contains a single phase named `test`, the component type is `TEST`. Otherwise, the component type is `BUILD`.

## Syntax
<a name="aws-resource-imagebuilder-component-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-imagebuilder-component-syntax.json"></a>

```
{
  "Type" : "AWS::ImageBuilder::Component",
  "Properties" : {
      "[ChangeDescription](#cfn-imagebuilder-component-changedescription)" : {{String}},
      "[Data](#cfn-imagebuilder-component-data)" : {{String}},
      "[Description](#cfn-imagebuilder-component-description)" : {{String}},
      "[KmsKeyId](#cfn-imagebuilder-component-kmskeyid)" : {{String}},
      "[Name](#cfn-imagebuilder-component-name)" : {{String}},
      "[Platform](#cfn-imagebuilder-component-platform)" : {{String}},
      "[SupportedOsVersions](#cfn-imagebuilder-component-supportedosversions)" : {{[ String, ... ]}},
      "[Tags](#cfn-imagebuilder-component-tags)" : {{{{{Key}}: {{Value}}, ...}}},
      "[Uri](#cfn-imagebuilder-component-uri)" : {{String}},
      "[Version](#cfn-imagebuilder-component-version)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-imagebuilder-component-syntax.yaml"></a>

```
Type: AWS::ImageBuilder::Component
Properties:
  [ChangeDescription](#cfn-imagebuilder-component-changedescription): {{String}}
  [Data](#cfn-imagebuilder-component-data): {{String}}
  [Description](#cfn-imagebuilder-component-description): {{String}}
  [KmsKeyId](#cfn-imagebuilder-component-kmskeyid): {{String}}
  [Name](#cfn-imagebuilder-component-name): {{String}}
  [Platform](#cfn-imagebuilder-component-platform): {{String}}
  [SupportedOsVersions](#cfn-imagebuilder-component-supportedosversions): {{
    - String}}
  [Tags](#cfn-imagebuilder-component-tags): {{
    {{Key}}: {{Value}}}}
  [Uri](#cfn-imagebuilder-component-uri): {{String}}
  [Version](#cfn-imagebuilder-component-version): {{String}}
```

## Properties
<a name="aws-resource-imagebuilder-component-properties"></a>

`ChangeDescription`  <a name="cfn-imagebuilder-component-changedescription"></a>
The change description of the component. Describes what change has been made in this version, or what makes this version different from other versions of the component.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Data`  <a name="cfn-imagebuilder-component-data"></a>
Component `data` contains inline YAML document content for the component. Alternatively, you can specify the `uri` of a YAML document file stored in Amazon S3. However, you cannot specify both properties.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `16000`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-imagebuilder-component-description"></a>
Describes the contents of the component.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`KmsKeyId`  <a name="cfn-imagebuilder-component-kmskeyid"></a>
The Amazon Resource Name (ARN) that uniquely identifies the KMS key used to encrypt this component. This can be either the Key ARN or the Alias ARN. For more information, see [Key identifiers (KeyId)](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN) in the *AWS Key Management Service Developer Guide*. If you don't specify a key, Image Builder encrypts the component data with a KMS key that Image Builder owns.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-imagebuilder-component-name"></a>
The name of the component. Image Builder generates the component ARN from a normalized form of the name, so names that differ only in case, spaces, or underscores count as the same name. If a component with the same name and semantic version already exists in your account in the same AWS Region, the request creates a new build version for it. If the content is also identical to the latest build version, the request fails because the component already exists.
*Required*: Yes
*Type*: String
*Pattern*: `^[-_A-Za-z-0-9][-_A-Za-z0-9 ]{1,126}[-_A-Za-z-0-9]$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Platform`  <a name="cfn-imagebuilder-component-platform"></a>
The operating system platform of the component.
*Required*: Yes
*Type*: String
*Allowed values*: `Windows | Linux | macOS`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SupportedOsVersions`  <a name="cfn-imagebuilder-component-supportedosversions"></a>
The operating system (OS) version supported by the component. If the OS information is available, a prefix match is performed against the base image OS version during image recipe creation.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `25`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-imagebuilder-component-tags"></a>
The tags that apply to the component.
*Required*: No
*Type*: Object of String
*Pattern*: `.{1,}`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Uri`  <a name="cfn-imagebuilder-component-uri"></a>
The `uri` of a YAML component document file. This must be an S3 URL (`s3://bucket/key`), and you must have permission to access the S3 bucket it points to. If you use Amazon S3, you can specify component content up to your service quota for component size, which is 64 KB by default.
Alternatively, you can specify the YAML document inline, using the component `data` property. You cannot specify both properties.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Version`  <a name="cfn-imagebuilder-component-version"></a>
The semantic version of the component. This version follows the semantic version syntax.
The semantic version has four nodes: <major>.<minor>.<patch>/<build>. You can assign values for the first three, and can filter on all of them.
**Assignment:** For the first three nodes, you can assign any positive integer value, including zero. The upper limit is 2^30-1, or 1073741823, for each node. Image Builder automatically assigns the build number to the fourth node.
**Patterns:** You can use any numeric pattern that adheres to the assignment requirements for the nodes that you can assign. For example, you might choose a software version pattern, such as 1.0.0, or a date, such as 2021.01.01.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9]+\.[0-9]+\.[0-9]+$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-imagebuilder-component-return-values"></a>

### Ref
<a name="aws-resource-imagebuilder-component-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the resource ARN, such as `arn:aws:imagebuilder:us-west-2:111122223333:component/examplecomponent/2019.12.02/1`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-imagebuilder-component-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-imagebuilder-component-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Returns the Amazon Resource Name (ARN) of the component. For example, `arn:aws:imagebuilder:us-west-2:111122223333:component/examplecomponent/2019.12.02/1`.

`Encrypted`  <a name="Encrypted-fn::getatt"></a>
Returns the encryption status of the component. For example `true` or `false`.

`LatestVersion.Arn`  <a name="LatestVersion.Arn-fn::getatt"></a>
The latest version Amazon Resource Name (ARN) of the Image Builder resource.

`LatestVersion.Major`  <a name="LatestVersion.Major-fn::getatt"></a>
The latest version Amazon Resource Name (ARN) with the same `major` version of the Image Builder resource.

`LatestVersion.Minor`  <a name="LatestVersion.Minor-fn::getatt"></a>
The latest version Amazon Resource Name (ARN) with the same `minor` version of the Image Builder resource.

`LatestVersion.Patch`  <a name="LatestVersion.Patch-fn::getatt"></a>
The latest version Amazon Resource Name (ARN) with the same `patch` version of the Image Builder resource.

`Name`  <a name="Name-fn::getatt"></a>
Returns the name of the component.

`Type`  <a name="Type-fn::getatt"></a>
Image Builder determines the component type based on the phases that are defined in the component document. If there is only one phase, and its name is "test", then the type is `TEST`. For all other components, the type is `BUILD`.

## Examples
<a name="aws-resource-imagebuilder-component--examples"></a>

**Topics**
+ [Create a component using Data](#aws-resource-imagebuilder-component--examples--Create_a_component_using_Data)
+ [Create a component using a Uri](#aws-resource-imagebuilder-component--examples--Create_a_component_using_a_Uri)

### Create a component using Data
<a name="aws-resource-imagebuilder-component--examples--Create_a_component_using_Data"></a>

The following example shows the template for the Component resource in both JSON and YAML format. This example includes details for the `Data` field. You can use either the `Data` or `Uri` fields to reference the component document.

#### JSON
<a name="aws-resource-imagebuilder-component--examples--Create_a_component_using_Data--json"></a>

```
{
	"Resources": {
		"ComponentAllParameters": {
			"Type": "AWS::ImageBuilder::Component",
			"Properties": {
				"Name": "component-name",
				"Platform": "Linux",
				"Version": "1.0.0",
				"Description": "description",
				"ChangeDescription": "change-description",
				"KmsKeyId": "customer-kms-key-id",
				"SupportedOsVersions": ["Amazon Linux 2"],
				"Tags": {
					"CustomerComponentTagKey1": "CustomerComponentTagValue1",
					"CustomerComponentTagKey2": "CustomerComponentTagValue2"
				},
				"Data": "name: HelloWorldTestingLinuxDoc - InlineData\ndescription: This is hello world testing doc\nschemaVersion: 1.0\n\nphases:\n  - name: build\n    steps:\n      - name: HelloWorldStep\n        action: ExecuteBash\n        inputs:\n          commands:\n            - echo \"Hello World! Build.\"\n  - name: validate\n    steps:\n      - name: HelloWorldStep\n        action: ExecuteBash\n        inputs:\n          commands:\n            - echo \"Hello World! Validate.\"\n  - name: test\n    steps:\n      - name: HelloWorldStep\n        action: ExecuteBash\n        inputs:\n          commands:\n            - echo \"Hello World! Test.\"\n"
			}
		}
	}
}
```

#### YAML
<a name="aws-resource-imagebuilder-component--examples--Create_a_component_using_Data--yaml"></a>

```
Resources:
  ComponentAllParameters:
    Type: 'AWS::ImageBuilder::Component'
    Properties:
      Name: 'component-name'
      Platform: 'Linux'
      Version: '1.0.0'
      Description: 'description'
      ChangeDescription: 'change-description'
      KmsKeyId: 'customer-kms-key-id'
      SupportedOsVersions:
        - 'Amazon Linux 2'
      Tags:
        CustomerComponentTagKey1: 'CustomerComponentTagValue1'
        CustomerComponentTagKey2: 'CustomerComponentTagValue2'
      # Require one of 'Data' or 'Uri' for Component template
      Data: |
        name: HelloWorldTestingLinuxDoc - InlineData
        description: This is hello world testing doc
        schemaVersion: 1.0

        phases:
          - name: build
            steps:
              - name: HelloWorldStep
                action: ExecuteBash
                inputs:
                  commands:
                    - echo "Hello World! Build."
          - name: validate
            steps:
              - name: HelloWorldStep
                action: ExecuteBash
                inputs:
                  commands:
                    - echo "Hello World! Validate."
          - name: test
            steps:
              - name: HelloWorldStep
                action: ExecuteBash
                inputs:
                  commands:
                    - echo "Hello World! Test."
```

### Create a component using a Uri
<a name="aws-resource-imagebuilder-component--examples--Create_a_component_using_a_Uri"></a>

The following example shows the template for the Component resource in both YAML and JSON format. This example includes details for the `Uri` field. You can use either the `Data` or `Uri` fields to reference the component document.

#### YAML
<a name="aws-resource-imagebuilder-component--examples--Create_a_component_using_a_Uri--yaml"></a>

```
Resources:
  ComponentAllParameters:
    Type: 'AWS::ImageBuilder::Component'
    Properties:
      Name: 'component-name'
      Platform: 'Linux'
      Version: '1.0.0'
      # Require one of 'Data' or 'Uri' for Component template
      Uri: 's3://imagebuilder/component_document.yml'
      Description: 'description'
      ChangeDescription: 'change-description'
      KmsKeyId: 'customer-kms-key-id'
      SupportedOsVersions:
        - 'CentOS'
        - 'Red Hat Enterprise Linux'
      Tags:
        CustomerComponentTagKey1: 'CustomerComponentTagValue1'
        CustomerComponentTagKey2: 'CustomerComponentTagValue2'
```

#### JSON
<a name="aws-resource-imagebuilder-component--examples--Create_a_component_using_a_Uri--json"></a>

```
{
    "Resources": {
        "ComponentAllParameters": {
            "Type": "AWS::ImageBuilder::Component",
            "Properties": {
                "Name": "component-name",
                "Platform": "Linux",
                "Version": "1.0.0",
                "Uri": "s3://imagebuilder/component_document.yml",
                "Description": "description",
                "ChangeDescription": "change-description",
                "KmsKeyId": "customer-kms-key-id",
                "SupportedOsVersions": ["CentOS", "Red Hat Enterprise Linux"],
                "Tags": {
                    "CustomerComponentTagKey1": "CustomerComponentTagValue1",
                    "CustomerComponentTagKey2": "CustomerComponentTagValue2"
                }
            }
        }
    }
}
```

## See also
<a name="aws-resource-imagebuilder-component--seealso"></a>
+ [Manage components with Image Builder](https://docs.aws.amazon.com/imagebuilder/latest/userguide/manage-components.html) in the *Image Builder User Guide*.
