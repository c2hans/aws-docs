---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutBucketReplication.html
---

# PutBucketReplication
<a name="API_control_PutBucketReplication"></a>

**Note**
This action creates an Amazon S3 on Outposts bucket's replication configuration. To create an S3 bucket's replication configuration, see [PutBucketReplication](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketReplication.html) in the *Amazon S3 API Reference*.

Creates a replication configuration or replaces an existing one. For information about S3 replication on Outposts configuration, see [Replicating objects for S3 on Outposts](https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3OutpostsReplication.html) in the *Amazon S3 User Guide*.

**Note**
It can take a while to propagate `PUT` or `DELETE` requests for a replication configuration to all S3 on Outposts systems. Therefore, the replication configuration that's returned by a `GET` request soon after a `PUT` or `DELETE` request might return a more recent result than what's on the Outpost. If an Outpost is offline, the delay in updating the replication configuration on that Outpost can be significant.

Specify the replication configuration in the request body. In the replication configuration, you provide the following information:
+ The name of the destination bucket or buckets where you want S3 on Outposts to replicate objects
+ The AWS Identity and Access Management (IAM) role that S3 on Outposts can assume to replicate objects on your behalf
+ Other relevant information, such as replication rules

A replication configuration must include at least one rule and can contain a maximum of 100. Each rule identifies a subset of objects to replicate by filtering the objects in the source Outposts bucket. To choose additional subsets of objects to replicate, add a rule for each subset.

To specify a subset of the objects in the source Outposts bucket to apply a replication rule to, add the `Filter` element as a child of the `Rule` element. You can filter objects based on an object key prefix, one or more object tags, or both. When you add the `Filter` element in the configuration, you must also add the following elements: `DeleteMarkerReplication`, `Status`, and `Priority`.

Using `PutBucketReplication` on Outposts requires that both the source and destination buckets must have versioning enabled. For information about enabling versioning on a bucket, see [Managing S3 Versioning for your S3 on Outposts bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3OutpostsManagingVersioning.html).

For information about S3 on Outposts replication failure reasons, see [Replication failure reasons](https://docs.aws.amazon.com/AmazonS3/latest/userguide/outposts-replication-eventbridge.html#outposts-replication-failure-codes) in the *Amazon S3 User Guide*.

 **Handling Replication of Encrypted Objects**

Outposts buckets are encrypted at all times. All the objects in the source Outposts bucket are encrypted and can be replicated. Also, all the replicas in the destination Outposts bucket are encrypted with the same encryption key as the objects in the source Outposts bucket.

 **Permissions**

To create a `PutBucketReplication` request, you must have `s3-outposts:PutReplicationConfiguration` permissions for the bucket. The Outposts bucket owner has this permission by default and can grant it to others. For more information about permissions, see [Setting up IAM with S3 on Outposts](https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3OutpostsIAM.html) and [Managing access to S3 on Outposts buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3OutpostsBucketPolicy.html).

**Note**
To perform this operation, the user or role must also have the `iam:CreateRole` and `iam:PassRole` permissions. For more information, see [Granting a user permissions to pass a role to an AWS service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html).

All Amazon S3 on Outposts REST API requests for this action require an additional parameter of `x-amz-outpost-id` to be passed with the request. In addition, you must use an S3 on Outposts endpoint hostname prefix instead of `s3-control`. For an example of the request syntax for Amazon S3 on Outposts that uses the S3 on Outposts endpoint hostname prefix and the `x-amz-outpost-id` derived by using the access point ARN, see the [Examples](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutBucketReplication.html#API_control_PutBucketReplication_Examples) section.

The following operations are related to `PutBucketReplication`:
+  [GetBucketReplication](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetBucketReplication.html)
+  [DeleteBucketReplication](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteBucketReplication.html)

## Request Syntax
<a name="API_control_PutBucketReplication_RequestSyntax"></a>

```
PUT /v20180820/bucket/{{name}}/replication HTTP/1.1
Host: {{Bucket}}.s3-control.amazonaws.com
x-amz-account-id: {{AccountId}}
<?xml version="1.0" encoding="UTF-8"?>
<ReplicationConfiguration xmlns="http://awss3control.amazonaws.com/doc/2018-08-20/">
   <Role>{{string}}</Role>
   <Rules>
      <Rule>
         <Bucket>{{string}}</Bucket>
         <DeleteMarkerReplication>
            <Status>{{string}}</Status>
         </DeleteMarkerReplication>
         <Destination>
            <AccessControlTranslation>
               <Owner>{{string}}</Owner>
            </AccessControlTranslation>
            <Account>{{string}}</Account>
            <Bucket>{{string}}</Bucket>
            <EncryptionConfiguration>
               <ReplicaKmsKeyID>{{string}}</ReplicaKmsKeyID>
            </EncryptionConfiguration>
            <Metrics>
               <EventThreshold>
                  <Minutes>{{integer}}</Minutes>
               </EventThreshold>
               <Status>{{string}}</Status>
            </Metrics>
            <ReplicationTime>
               <Status>{{string}}</Status>
               <Time>
                  <Minutes>{{integer}}</Minutes>
               </Time>
            </ReplicationTime>
            <StorageClass>{{string}}</StorageClass>
         </Destination>
         <ExistingObjectReplication>
            <Status>{{string}}</Status>
         </ExistingObjectReplication>
         <Filter>
            <And>
               <Prefix>{{string}}</Prefix>
               <Tags>
                  <S3Tag>
                     <Key>{{string}}</Key>
                     <Value>{{string}}</Value>
                  </S3Tag>
               </Tags>
            </And>
            <Prefix>{{string}}</Prefix>
            <Tag>
               <Key>{{string}}</Key>
               <Value>{{string}}</Value>
            </Tag>
         </Filter>
         <ID>{{string}}</ID>
         <Prefix>{{string}}</Prefix>
         <Priority>{{integer}}</Priority>
         <SourceSelectionCriteria>
            <ReplicaModifications>
               <Status>{{string}}</Status>
            </ReplicaModifications>
            <SseKmsEncryptedObjects>
               <Status>{{string}}</Status>
            </SseKmsEncryptedObjects>
         </SourceSelectionCriteria>
         <Status>{{string}}</Status>
      </Rule>
   </Rules>
</ReplicationConfiguration>
```

## URI Request Parameters
<a name="API_control_PutBucketReplication_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_control_PutBucketReplication_RequestSyntax) **   <a name="AmazonS3-control_PutBucketReplication-request-header-Bucket"></a>
Specifies the S3 on Outposts bucket to set the configuration for.
For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.
For using this parameter with S3 on Outposts with the AWS SDK and CLI, you must specify the ARN of the bucket accessed in the format `arn:aws:s3-outposts:<Region>:<account-id>:outpost/<outpost-id>/bucket/<my-bucket-name>`. For example, to access the bucket `reports` through Outpost `my-outpost` owned by account `123456789012` in Region `us-west-2`, use the URL encoding of `arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/bucket/reports`. The value must be URL encoded.
Length Constraints: Minimum length of 3. Maximum length of 255.
Required: Yes

 ** [x-amz-account-id](#API_control_PutBucketReplication_RequestSyntax) **   <a name="AmazonS3-control_PutBucketReplication-request-header-AccountId"></a>
The AWS account ID of the Outposts bucket.
Length Constraints: Maximum length of 64.
Pattern: `^\d{12}$`
Required: Yes

## Request Body
<a name="API_control_PutBucketReplication_RequestBody"></a>

The request accepts the following data in XML format.

 ** [ReplicationConfiguration](#API_control_PutBucketReplication_RequestSyntax) **   <a name="AmazonS3-control_PutBucketReplication-request-ReplicationConfiguration"></a>
Root level tag for the ReplicationConfiguration parameters.
Required: Yes

 ** [Role](#API_control_PutBucketReplication_RequestSyntax) **   <a name="AmazonS3-control_PutBucketReplication-request-Role"></a>
The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that S3 on Outposts assumes when replicating objects. For information about S3 replication on Outposts configuration, see [Setting up replication](https://docs.aws.amazon.com/AmazonS3/latest/userguide/outposts-replication-how-setup.html) in the *Amazon S3 User Guide*.
Type: String
Required: Yes

 ** [Rules](#API_control_PutBucketReplication_RequestSyntax) **   <a name="AmazonS3-control_PutBucketReplication-request-Rules"></a>
A container for one or more replication rules. A replication configuration must have at least one rule and can contain an array of 100 rules at the most.
Type: Array of [ReplicationRule](API_control_ReplicationRule.md) data types
Required: Yes

## Response Syntax
<a name="API_control_PutBucketReplication_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_control_PutBucketReplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Examples
<a name="API_control_PutBucketReplication_Examples"></a>

### Sample Request: Add a replication configuration to an Amazon S3 on Outposts bucket
<a name="API_control_PutBucketReplication_Example_1"></a>

The following sample `PUT` request creates a replication subresource on the specified Outposts bucket named `example-outpost-bucket` and saves the replication configuration in it. The replication configuration specifies a rule to replicate objects to the `example-outpost-bucket` bucket. The rule includes a filter to replicate only the objects that are created with the key name prefix `TaxDocs` and that have two specific tags.

After you add a replication configuration to your Outposts bucket, S3 on Outposts assumes the AWS Identity and Access Management (IAM) role that's specified in the configuration to replicate objects on behalf of the Outposts bucket owner. The bucket owner is the AWS account that created the Outposts bucket.

Filtering by using the `Filter` element is supported in the latest XML configuration. The earlier version of the XML configuration isn't supported.

For more examples of S3 replication on Outposts configuration, see [Creating replication rules on Outposts](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication-between-outposts.html) in the *Amazon S3 User Guide*.

```
PUT /v20180820/bucket/example-outpost-bucket/replication HTTP/1.1
Host:s3-outposts.<Region>.amazonaws.com
x-amz-account-id: example-account-id
x-amz-outpost-id: op-01ac5d28a6a232904
Authorization: authorization string

<ReplicationConfiguration>
  <Role>arn:aws:iam::35667example:role/ReplicationRoleForS3Outposts</Role>
  <Rules>
   <Rule>
      <Bucket>arn:aws:s3-outposts:us-east-1:example-account-id:outpost/SOURCE-OUTPOST-ID/accesspoint/SOURCE-OUTPOSTS-BUCKET-ACCESS-POINT</Bucket>
      <ID>rule1</ID>
      <Status>Enabled</Status>
      <Priority>1</Priority>
      <DeleteMarkerReplication>
         <Status>Disabled</Status>
      </DeleteMarkerReplication>
      <Filter>
         <And>
            <Prefix>TaxDocs</Prefix>
            <Tag>
               <Key>key1</Key>
               <Value>value1</Value>
            </Tag>
            <Tag>
               <Key>key2</Key>
               <Value>value2</Value>
            </Tag>
         </And>
      </Filter>
      <Destination>
         <Bucket>arn:aws:s3-outposts:us-east-1:example-account-id:outpost/DESTINATION-OUTPOST-ID/accesspoint/DESTINATION-OUTPOSTS-BUCKET-ACCESS-POINT</Bucket>
      </Destination>
   </Rule>
  </Rules>
</ReplicationConfiguration>
```

## See Also
<a name="API_control_PutBucketReplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/PutBucketReplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3control-2018-08-20/PutBucketReplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/PutBucketReplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/PutBucketReplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/PutBucketReplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/PutBucketReplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/PutBucketReplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/PutBucketReplication)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/PutBucketReplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/PutBucketReplication)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
