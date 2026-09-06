---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_NetworkMigrationCodeGenerationArtifact.html
---

# NetworkMigrationCodeGenerationArtifact
<a name="API_NetworkMigrationCodeGenerationArtifact"></a>

An artifact generated during code generation, such as a CloudFormation template or Terraform file.

## Contents
<a name="API_NetworkMigrationCodeGenerationArtifact_Contents"></a>

 ** artifactID **   <a name="mgn-Type-NetworkMigrationCodeGenerationArtifact-artifactID"></a>
The unique identifier of the artifact.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** artifactSubType **   <a name="mgn-Type-NetworkMigrationCodeGenerationArtifact-artifactSubType"></a>
The sub-type of the artifact for further classification.
Type: String
Valid Values: `APPLICATION | NESTED_STACK | STACK`
Required: No

 ** artifactType **   <a name="mgn-Type-NetworkMigrationCodeGenerationArtifact-artifactType"></a>
The type of the generated artifact.
Type: String
Valid Values: `CDK_TYPESCRIPT | CLOUDFORMATION_TEMPLATE | CDKTF_TYPESCRIPT | TERRAFORM_CONFIGURATION | CDK_L2_TYPESCRIPT`
Required: No

 ** checksum **   <a name="mgn-Type-NetworkMigrationCodeGenerationArtifact-checksum"></a>
The checksum of the artifact for integrity verification.
Type: [Checksum](API_Checksum.md) object
Required: No

 ** createdAt **   <a name="mgn-Type-NetworkMigrationCodeGenerationArtifact-createdAt"></a>
The timestamp when the artifact was created.
Type: Timestamp
Required: No

 ** logicalID **   <a name="mgn-Type-NetworkMigrationCodeGenerationArtifact-logicalID"></a>
The logical identifier for the artifact.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z][a-zA-Z0-9-]*`
Required: No

 ** outputS3Configuration **   <a name="mgn-Type-NetworkMigrationCodeGenerationArtifact-outputS3Configuration"></a>
The S3 location where the artifact is stored.
Type: [S3Configuration](API_S3Configuration.md) object
Required: No

## See Also
<a name="API_NetworkMigrationCodeGenerationArtifact_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/NetworkMigrationCodeGenerationArtifact)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/NetworkMigrationCodeGenerationArtifact)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/NetworkMigrationCodeGenerationArtifact)
