---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_SeveritySummary.html
---

# SeveritySummary
<a name="API_SeveritySummary"></a>

The number of managed nodes found for each patch severity level defined in the request filter.

## Contents
<a name="API_SeveritySummary_Contents"></a>

 ** CriticalCount **   <a name="systemsmanager-Type-SeveritySummary-CriticalCount"></a>
The total number of resources or compliance items that have a severity level of `Critical`. Critical severity is determined by the organization that published the compliance items.
Type: Integer
Required: No

 ** HighCount **   <a name="systemsmanager-Type-SeveritySummary-HighCount"></a>
The total number of resources or compliance items that have a severity level of high. High severity is determined by the organization that published the compliance items.
Type: Integer
Required: No

 ** InformationalCount **   <a name="systemsmanager-Type-SeveritySummary-InformationalCount"></a>
The total number of resources or compliance items that have a severity level of informational. Informational severity is determined by the organization that published the compliance items.
Type: Integer
Required: No

 ** LowCount **   <a name="systemsmanager-Type-SeveritySummary-LowCount"></a>
The total number of resources or compliance items that have a severity level of low. Low severity is determined by the organization that published the compliance items.
Type: Integer
Required: No

 ** MediumCount **   <a name="systemsmanager-Type-SeveritySummary-MediumCount"></a>
The total number of resources or compliance items that have a severity level of medium. Medium severity is determined by the organization that published the compliance items.
Type: Integer
Required: No

 ** UnspecifiedCount **   <a name="systemsmanager-Type-SeveritySummary-UnspecifiedCount"></a>
The total number of resources or compliance items that have a severity level of unspecified. Unspecified severity is determined by the organization that published the compliance items.
Type: Integer
Required: No

## See Also
<a name="API_SeveritySummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/SeveritySummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/SeveritySummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/SeveritySummary)
