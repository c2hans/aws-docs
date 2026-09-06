---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_HoursOfOperation.html
---

# HoursOfOperation
<a name="API_HoursOfOperation"></a>

Information about of the hours of operation.

## Contents
<a name="API_HoursOfOperation_Contents"></a>

 ** Config **   <a name="connect-Type-HoursOfOperation-Config"></a>
Configuration information for the hours of operation.
Type: Array of [HoursOfOperationConfig](API_HoursOfOperationConfig.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 ** Description **   <a name="connect-Type-HoursOfOperation-Description"></a>
The description for the hours of operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 250.
Required: No

 ** HoursOfOperationArn **   <a name="connect-Type-HoursOfOperation-HoursOfOperationArn"></a>
The Amazon Resource Name (ARN) for the hours of operation.
Type: String
Required: No

 ** HoursOfOperationId **   <a name="connect-Type-HoursOfOperation-HoursOfOperationId"></a>
The identifier for the hours of operation.
Type: String
Required: No

 ** LastModifiedRegion **   <a name="connect-Type-HoursOfOperation-LastModifiedRegion"></a>
The AWS Region where this resource was last modified.
Type: String
Pattern: `[a-z]{2}(-[a-z]+){1,2}(-[0-9])?`
Required: No

 ** LastModifiedTime **   <a name="connect-Type-HoursOfOperation-LastModifiedTime"></a>
The timestamp when this resource was last modified.
Type: Timestamp
Required: No

 ** Name **   <a name="connect-Type-HoursOfOperation-Name"></a>
The name for the hours of operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Required: No

 ** ParentHoursOfOperations **   <a name="connect-Type-HoursOfOperation-ParentHoursOfOperations"></a>
Information about parent hours of operations.
Type: Array of [HoursOfOperationsIdentifier](API_HoursOfOperationsIdentifier.md) objects
Required: No

 ** Tags **   <a name="connect-Type-HoursOfOperation-Tags"></a>
The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

 ** TimeZone **   <a name="connect-Type-HoursOfOperation-TimeZone"></a>
The time zone for the hours of operation.
Type: String
Required: No

## See Also
<a name="API_HoursOfOperation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/HoursOfOperation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/HoursOfOperation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/HoursOfOperation)
