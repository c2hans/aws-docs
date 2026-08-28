---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-datasync-locationobjectstorage.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataSync::LocationObjectStorage
<a name="aws-resource-datasync-locationobjectstorage"></a>

The `AWS::DataSync::LocationObjectStorage` resource specifies an endpoint for a self-managed object storage bucket. For more information about self-managed object storage locations, see [Creating a Location for Object Storage](https://docs.aws.amazon.com/datasync/latest/userguide/create-object-location.html).

## Syntax
<a name="aws-resource-datasync-locationobjectstorage-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-datasync-locationobjectstorage-syntax.json"></a>

```
{
  "Type" : "AWS::DataSync::LocationObjectStorage",
  "Properties" : {
      "[AccessKey](#cfn-datasync-locationobjectstorage-accesskey)" : {{String}},
      "[AgentArns](#cfn-datasync-locationobjectstorage-agentarns)" : {{[ String, ... ]}},
      "[BucketName](#cfn-datasync-locationobjectstorage-bucketname)" : {{String}},
      "[CmkSecretConfig](#cfn-datasync-locationobjectstorage-cmksecretconfig)" : {{CmkSecretConfig}},
      "[CustomSecretConfig](#cfn-datasync-locationobjectstorage-customsecretconfig)" : {{CustomSecretConfig}},
      "[SecretKey](#cfn-datasync-locationobjectstorage-secretkey)" : {{String}},
      "[ServerCertificate](#cfn-datasync-locationobjectstorage-servercertificate)" : {{String}},
      "[ServerHostname](#cfn-datasync-locationobjectstorage-serverhostname)" : {{String}},
      "[ServerPort](#cfn-datasync-locationobjectstorage-serverport)" : {{Integer}},
      "[ServerProtocol](#cfn-datasync-locationobjectstorage-serverprotocol)" : {{String}},
      "[Subdirectory](#cfn-datasync-locationobjectstorage-subdirectory)" : {{String}},
      "[Tags](#cfn-datasync-locationobjectstorage-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-datasync-locationobjectstorage-syntax.yaml"></a>

```
Type: AWS::DataSync::LocationObjectStorage
Properties:
  [AccessKey](#cfn-datasync-locationobjectstorage-accesskey): {{String}}
  [AgentArns](#cfn-datasync-locationobjectstorage-agentarns): {{
    - String}}
  [BucketName](#cfn-datasync-locationobjectstorage-bucketname): {{String}}
  [CmkSecretConfig](#cfn-datasync-locationobjectstorage-cmksecretconfig): {{
    CmkSecretConfig}}
  [CustomSecretConfig](#cfn-datasync-locationobjectstorage-customsecretconfig): {{
    CustomSecretConfig}}
  [SecretKey](#cfn-datasync-locationobjectstorage-secretkey): {{String}}
  [ServerCertificate](#cfn-datasync-locationobjectstorage-servercertificate): {{String}}
  [ServerHostname](#cfn-datasync-locationobjectstorage-serverhostname): {{String}}
  [ServerPort](#cfn-datasync-locationobjectstorage-serverport): {{Integer}}
  [ServerProtocol](#cfn-datasync-locationobjectstorage-serverprotocol): {{String}}
  [Subdirectory](#cfn-datasync-locationobjectstorage-subdirectory): {{String}}
  [Tags](#cfn-datasync-locationobjectstorage-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-datasync-locationobjectstorage-properties"></a>

`AccessKey`  <a name="cfn-datasync-locationobjectstorage-accesskey"></a>
Specifies the access key (for example, a user name) if credentials are required to authenticate with the object storage server.
*Required*: No
*Type*: String
*Pattern*: `^.+$`
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AgentArns`  <a name="cfn-datasync-locationobjectstorage-agentarns"></a>
(Optional) Specifies the Amazon Resource Names (ARNs) of the DataSync agents that can connect with your object storage system. If you are setting up an agentless cross-cloud transfer, you do not need to specify a value for this parameter.
Make sure you configure this parameter correctly when you first create your storage location. You cannot add or remove agents from a storage location after you create it.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `128 | 8`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BucketName`  <a name="cfn-datasync-locationobjectstorage-bucketname"></a>
Specifies the name of the object storage bucket involved in the transfer.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9_\-\+\./\(\)\$\p{Zs}]+$`
*Minimum*: `3`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CmkSecretConfig`  <a name="cfn-datasync-locationobjectstorage-cmksecretconfig"></a>
Specifies configuration information for a DataSync-managed secret, which includes the `SecretKey` that DataSync uses to access a specific object storage location, with a customer-managed AWS KMS key.
When you include this parameter as part of a `CreateLocationObjectStorage` request, you provide only the KMS key ARN. DataSync uses this KMS key together with the value you specify for the `SecretKey` parameter to create a DataSync-managed secret to store the location access credentials.
Make sure that DataSync has permission to access the KMS key that you specify. For more information, see [ Using a service-managed secret encrypted with a custom AWS KMS key](https://docs.aws.amazon.com/datasync/latest/userguide/location-credentials.html#service-secret-custom-key).
You can use either `CmkSecretConfig` (with `SecretKey`) or `CustomSecretConfig` (without `SecretKey`) to provide credentials for a `CreateLocationObjectStorage` request. Do not provide both parameters for the same request.
*Required*: No
*Type*: [CmkSecretConfig](aws-properties-datasync-locationobjectstorage-cmksecretconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomSecretConfig`  <a name="cfn-datasync-locationobjectstorage-customsecretconfig"></a>
Specifies configuration information for a customer-managed Secrets Manager secret where the secret key for a specific object storage location is stored in plain text, in Secrets Manager. This configuration includes the secret ARN, and the ARN for an IAM role that provides access to the secret. For more information, see [ Using a secret that you manage](https://docs.aws.amazon.com/datasync/latest/userguide/location-credentials.html#custom-secret-custom-key).
You can use either `CmkSecretConfig` (with `SecretKey`) or `CustomSecretConfig` (without `SecretKey`) to provide credentials for a `CreateLocationObjectStorage` request. Do not provide both parameters for the same request.
*Required*: No
*Type*: [CustomSecretConfig](aws-properties-datasync-locationobjectstorage-customsecretconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecretKey`  <a name="cfn-datasync-locationobjectstorage-secretkey"></a>
Specifies the secret key (for example, a password) if credentials are required to authenticate with the object storage server.
If you provide a secret using `SecretKey`, but do not provide secret configuration details using `CmkSecretConfig` or `CustomSecretConfig`, then DataSync stores the token using your AWS account's Secrets Manager secret.
*Required*: No
*Type*: String
*Pattern*: `^.+$`
*Minimum*: `8`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServerCertificate`  <a name="cfn-datasync-locationobjectstorage-servercertificate"></a>
Specifies a certificate chain for DataSync to authenticate with your object storage system if the system uses a private or self-signed certificate authority (CA). You must specify a single `.pem` file with a full certificate chain (for example, `file:///home/user/.ssh/object_storage_certificates.pem`).
The certificate chain might include:
+ The object storage system's certificate
+ All intermediate certificates (if there are any)
+ The root certificate of the signing CA
You can concatenate your certificates into a `.pem` file (which can be up to 32768 bytes before base64 encoding). The following example `cat` command creates an `object_storage_certificates.pem` file that includes three certificates:
 `cat object_server_certificate.pem intermediate_certificate.pem ca_root_certificate.pem > object_storage_certificates.pem`
To use this parameter, configure `ServerProtocol` to `HTTPS`.
*Required*: No
*Type*: String
*Maximum*: `32768`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServerHostname`  <a name="cfn-datasync-locationobjectstorage-serverhostname"></a>
Specifies the domain name or IP address (IPv4 or IPv6) of the object storage server that your DataSync agent connects to.
*Required*: No
*Type*: String
*Pattern*: `^(([a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9\-]*[A-Za-z0-9])$`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServerPort`  <a name="cfn-datasync-locationobjectstorage-serverport"></a>
Specifies the port that your object storage server accepts inbound network traffic on (for example, port 443).
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `65536`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServerProtocol`  <a name="cfn-datasync-locationobjectstorage-serverprotocol"></a>
Specifies the protocol that your object storage server uses to communicate. If not specified, the default value is `HTTPS`.
*Required*: No
*Type*: String
*Allowed values*: `HTTPS | HTTP`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Subdirectory`  <a name="cfn-datasync-locationobjectstorage-subdirectory"></a>
Specifies the object prefix for your object storage server. If this is a source location, DataSync only copies objects with this prefix. If this is a destination location, DataSync writes all objects with this prefix.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9_\-\+\./\(\)\p{Zs}]*$`
*Maximum*: `4096`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-datasync-locationobjectstorage-tags"></a>
Specifies the key-value pair that represents a tag that you want to add to the resource. Tags can help you manage, filter, and search for your resources. We recommend creating a name tag for your location.
*Required*: No
*Type*: Array of [Tag](aws-properties-datasync-locationobjectstorage-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-datasync-locationobjectstorage-return-values"></a>

### Ref
<a name="aws-resource-datasync-locationobjectstorage-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the location resource Amazon Resource Name (ARN). For example:

 `arn:aws:datasync:us-east-2:111222333444:location/loc-07db7abfc326c50s3`

For more information about using the `Ref` function, see [Ref](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-datasync-locationobjectstorage-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-datasync-locationobjectstorage-return-values-fn--getatt-fn--getatt"></a>

`CmkSecretConfig.SecretArn`  <a name="CmkSecretConfig.SecretArn-fn::getatt"></a>
Property description not available.

`LocationArn`  <a name="LocationArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the specified object storage location.

`LocationUri`  <a name="LocationUri-fn::getatt"></a>
The URI of the specified object storage location.

## Examples
<a name="aws-resource-datasync-locationobjectstorage--examples"></a>

### Create an object storage location for DataSync
<a name="aws-resource-datasync-locationobjectstorage--examples--Create_an_object_storage_location_for_DataSync"></a>

The following example specifies an object storage location for DataSync. In this example, the object storage location uses the bucket named `MyBucket`, on the server named `MyServer@example.com`. This example also specifies the server protocol `HTTPS` and the subdirectory `/Subdirectory`.

#### JSON
<a name="aws-resource-datasync-locationobjectstorage--examples--Create_an_object_storage_location_for_DataSync--json"></a>

```
{
"AWSTemplateFormatVersion": "2010-09-09",
"Description": "Specifies an object storage location for DataSync",
"Resources":
{
  "LocationObjectStorage": {
    "Type": "AWS::DataSync::LocationObjectStorage",
    "Properties": {
      "AgentArns": [
        "arn:aws:datasync:us-east-2:111222333444:agent/agent-0b0addbeef44b3nfs"
      ],
      "BucketName": "MyBucket",
      "ServerHostname": "MyServer@example.com",
      "ServerProtocol": "HTTPS",
      "Subdirectory": "/MySubdirectory"
    }
  }
}
```

#### YAML
<a name="aws-resource-datasync-locationobjectstorage--examples--Create_an_object_storage_location_for_DataSync--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Description: Specifies an object storage location for DataSync
Resources:
  LocationObjectStorage:
    Type: AWS::DataSync::LocationObjectStorage
    Properties:
      AgentArns:
        - arn:aws:datasync:us-east-2:111222333444:agent/agent-0b0addbeef44b3nfs
      BucketName: MyBucket
      ServerHostname: MyServer@example.com
      ServerProtocol: HTTPS
      Subdirectory: /MySubdirectory
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
