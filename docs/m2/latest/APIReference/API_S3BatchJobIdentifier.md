---
source_url: https://docs.aws.amazon.com/m2/latest/APIReference/API_S3BatchJobIdentifier.html
---

# S3BatchJobIdentifier
<a name="API_S3BatchJobIdentifier"></a>

A batch job identifier in which the batch jobs to run are identified by an Amazon S3 location.

## Contents
<a name="API_S3BatchJobIdentifier_Contents"></a>

 ** bucket **   <a name="m2-Type-S3BatchJobIdentifier-bucket"></a>
The Amazon S3 bucket that contains the batch job definitions.
Type: String
Required: Yes

 ** identifier **   <a name="m2-Type-S3BatchJobIdentifier-identifier"></a>
Identifies the batch job definition. This identifier can also point to any batch job definition that already exists in the application or to one of the batch job definitions within the directory that is specified in `keyPrefix`.
Type: [JobIdentifier](API_JobIdentifier.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** keyPrefix **   <a name="m2-Type-S3BatchJobIdentifier-keyPrefix"></a>
The key prefix that specifies the path to the folder in the S3 bucket that has the batch job definitions.
Type: String
Required: No

## See Also
<a name="API_S3BatchJobIdentifier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/m2-2021-04-28/S3BatchJobIdentifier)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/m2-2021-04-28/S3BatchJobIdentifier)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/m2-2021-04-28/S3BatchJobIdentifier)
