---
source_url: https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_DatastoreProperties.html
---

# DatastoreProperties
<a name="API_DatastoreProperties"></a>

The properties associated with the data store.

## Contents
<a name="API_DatastoreProperties_Contents"></a>

 ** datastoreId **   <a name="healthimaging-Type-DatastoreProperties-datastoreId"></a>
The data store identifier.
Type: String
Pattern: `[0-9a-z]{32}`
Required: Yes

 ** datastoreName **   <a name="healthimaging-Type-DatastoreProperties-datastoreName"></a>
The data store name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9._/#-]+`
Required: Yes

 ** datastoreStatus **   <a name="healthimaging-Type-DatastoreProperties-datastoreStatus"></a>
The data store status.
Type: String
Valid Values: `CREATING | CREATE_FAILED | ACTIVE | DELETING | DELETED`
Required: Yes

 ** createdAt **   <a name="healthimaging-Type-DatastoreProperties-createdAt"></a>
The timestamp when the data store was created.
Type: Timestamp
Required: No

 ** datastoreArn **   <a name="healthimaging-Type-DatastoreProperties-datastoreArn"></a>
The Amazon Resource Name (ARN) for the data store.
Type: String
Pattern: `arn:aws((-us-gov)|(-iso)|(-iso-b)|(-cn))?:medical-imaging:[a-z0-9-]+:[0-9]{12}:datastore/[0-9a-z]{32}(/imageset/[0-9a-z]{32})?`
Required: No

 ** kmsKeyArn **   <a name="healthimaging-Type-DatastoreProperties-kmsKeyArn"></a>
The Amazon Resource Name (ARN) assigned to the Key Management Service (KMS) key for accessing encrypted data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `arn:aws[a-zA-Z-]{0,16}:kms:[a-z]{2}(-[a-z]{1,16}){1,3}-\d{1}:\d{12}:((key/[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12})|(alias/[a-zA-Z0-9:/_-]{1,256}))`
Required: No

 ** lambdaAuthorizerArn **   <a name="healthimaging-Type-DatastoreProperties-lambdaAuthorizerArn"></a>
The ARN of the authorizer's Lambda function.
Type: String
Pattern: `arn:(aws[a-zA-Z-]*)?:lambda:[a-z]{2}((-gov)|(-iso(b?)))?-[a-z]+-\d{1}:\d{12}:function:[a-zA-Z0-9-_]+(:(\$LATEST|[a-zA-Z0-9-_]+))?`
Required: No

 ** losslessStorageFormat **   <a name="healthimaging-Type-DatastoreProperties-losslessStorageFormat"></a>
The datastore's lossless storage format.
Type: String
Valid Values: `HTJ2K | JPEG_2000_LOSSLESS`
Required: No

 ** updatedAt **   <a name="healthimaging-Type-DatastoreProperties-updatedAt"></a>
The timestamp when the data store was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_DatastoreProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/medical-imaging-2023-07-19/DatastoreProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/medical-imaging-2023-07-19/DatastoreProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/medical-imaging-2023-07-19/DatastoreProperties)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthImaging. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query healthimaging` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
