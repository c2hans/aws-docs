---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_TargetResourceConfiguration.html
---

# TargetResourceConfiguration
<a name="API_TargetResourceConfiguration"></a>

The configuration for a single resource in the green environment of a blue/green deployment.

Use `SourceArn` to identify a resource in the blue environment. Amazon RDS creates the corresponding resource in the green environment using this configuration.

This data type is a request parameter of the `CreateBlueGreenDeployment` operation.

## Contents
<a name="API_TargetResourceConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** SourceArn **
The Amazon Resource Name (ARN) of the DB cluster or DB instance in the blue environment to which this configuration applies.
Type: String
Length Constraints: Minimum length of 39. Maximum length of 255.
Pattern: `arn:aws[a-z-]*:rds(-[a-z]+)?:[a-z0-9-]*:[0-9]{12}:(cluster|db):[a-zA-Z][a-zA-Z0-9-]{0,62}`
Required: Yes

 ** TargetKmsKeyId **
The AWS KMS key identifier for encryption of the corresponding resource in the green environment.
The AWS KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key.
Specify this setting in either of the following cases:
+ You want the green resource to use a different KMS key than the blue resource.
+ The blue resource is unencrypted and you want to encrypt the green resource.
For Aurora, encryption applies at the DB cluster level. Specify a DB cluster ARN in `SourceArn`. All DB instances in that cluster use the same KMS key.
For RDS, encryption applies at the DB instance level. Specify a DB instance ARN in `SourceArn`. To encrypt read replicas, include a separate entry for each one. Each entry can specify a different KMS key.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[a-zA-Z0-9_:\-\/]+`
Required: No

## See Also
<a name="API_TargetResourceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/TargetResourceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/TargetResourceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/TargetResourceConfiguration)
