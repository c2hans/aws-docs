---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_ObjectLockRetention.html
---

# ObjectLockRetention
<a name="API_ObjectLockRetention"></a>

A Retention configuration for an object.

## Contents
<a name="API_ObjectLockRetention_Contents"></a>

 ** EventHold **   <a name="AmazonS3-Type-ObjectLockRetention-EventHold"></a>
The event hold status for the object. Set to `ON` to enable an event hold or `OFF` to disable it.
Type: String
Valid Values: `ON | OFF`
Required: No

 ** EventHoldDuration **   <a name="AmazonS3-Type-ObjectLockRetention-EventHoldDuration"></a>
The event hold duration for the object. Specifies how long the object remains protected after the event hold is released.
Type: [EventHoldDuration](API_EventHoldDuration.md) data type
Required: No

 ** Mode **   <a name="AmazonS3-Type-ObjectLockRetention-Mode"></a>
Indicates the Retention mode for the specified object.
Type: String
Valid Values: `GOVERNANCE | COMPLIANCE`
Required: No

 ** RetainUntilDate **   <a name="AmazonS3-Type-ObjectLockRetention-RetainUntilDate"></a>
The date on which this Object Lock Retention will expire.
Type: Timestamp
Required: No

## See Also
<a name="API_ObjectLockRetention_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/ObjectLockRetention)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/ObjectLockRetention)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/ObjectLockRetention)
