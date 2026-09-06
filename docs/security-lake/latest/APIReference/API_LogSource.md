---
source_url: https://docs.aws.amazon.com/security-lake/latest/APIReference/API_LogSource.html
---

# LogSource
<a name="API_LogSource"></a>

Amazon Security Lake can collect logs and events from natively-supported AWS services and custom sources.

## Contents
<a name="API_LogSource_Contents"></a>

 ** account **   <a name="securitylake-Type-LogSource-account"></a>
Specify the account from which you want to collect logs.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: No

 ** region **   <a name="securitylake-Type-LogSource-region"></a>
Specify the Regions from which you want to collect logs.
Type: String
Pattern: `(us(-gov)?|af|ap|ca|eu|me|sa)-(central|north|(north(?:east|west))|south|south(?:east|west)|east|west)-\d+`
Required: No

 ** sources **   <a name="securitylake-Type-LogSource-sources"></a>
Specify the sources from which you want to collect logs.
Type: Array of [LogSourceResource](API_LogSourceResource.md) objects
Required: No

## See Also
<a name="API_LogSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securitylake-2018-05-10/LogSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securitylake-2018-05-10/LogSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securitylake-2018-05-10/LogSource)
