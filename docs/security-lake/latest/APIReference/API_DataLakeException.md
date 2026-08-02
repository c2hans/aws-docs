---
source_url: https://docs.aws.amazon.com/security-lake/latest/APIReference/API_DataLakeException.html
---

# DataLakeException
<a name="API_DataLakeException"></a>

The details for an Amazon Security Lake exception.

## Contents
<a name="API_DataLakeException_Contents"></a>

 ** exception **   <a name="securitylake-Type-DataLakeException-exception"></a>
The underlying exception of a Security Lake exception.
Type: String
Pattern: `[\\\w\-_:/.@=+]*`
Required: No

 ** region **   <a name="securitylake-Type-DataLakeException-region"></a>
The AWS Regions where the exception occurred.
Type: String
Pattern: `(us(-gov)?|af|ap|ca|eu|me|sa)-(central|north|(north(?:east|west))|south|south(?:east|west)|east|west)-\d+`
Required: No

 ** remediation **   <a name="securitylake-Type-DataLakeException-remediation"></a>
List of all remediation steps for a Security Lake exception.
Type: String
Pattern: `[\\\w\-_:/.@=+]*`
Required: No

 ** timestamp **   <a name="securitylake-Type-DataLakeException-timestamp"></a>
This error can occur if you configure the wrong timestamp format, or if the subset of entries used for validation had errors or missing values.
Type: Timestamp
Required: No

## See Also
<a name="API_DataLakeException_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securitylake-2018-05-10/DataLakeException)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securitylake-2018-05-10/DataLakeException)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securitylake-2018-05-10/DataLakeException)
