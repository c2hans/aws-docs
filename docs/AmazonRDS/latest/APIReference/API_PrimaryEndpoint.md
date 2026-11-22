---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_PrimaryEndpoint.html
---

# PrimaryEndpoint

Contains the information you need to connect to the DB instance that currently has the primary role. The endpoint stays the same when the primary role moves to another DB instance, so you don't have to connect to a different DNS name after a switchover.

## Contents
<a name="API_PrimaryEndpoint_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Address **
Specifies the DNS address of the DB instance that currently has the primary role. This address doesn't change when the DB instance is renamed.
Type: String
Required: No

 ** HostedZoneId **
Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.
Type: String
Required: No

## See Also
<a name="API_PrimaryEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/PrimaryEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/PrimaryEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/PrimaryEndpoint)
