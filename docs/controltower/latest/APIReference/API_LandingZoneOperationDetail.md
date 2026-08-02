---
source_url: https://docs.aws.amazon.com/controltower/latest/APIReference/API_LandingZoneOperationDetail.html
---

# LandingZoneOperationDetail
<a name="API_LandingZoneOperationDetail"></a>

Information about a landing zone operation.

## Contents
<a name="API_LandingZoneOperationDetail_Contents"></a>

 ** endTime **   <a name="controltower-Type-LandingZoneOperationDetail-endTime"></a>
The landing zone operation end time.
Type: Timestamp
Required: No

 ** operationIdentifier **   <a name="controltower-Type-LandingZoneOperationDetail-operationIdentifier"></a>
The `operationIdentifier` of the landing zone operation.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** operationType **   <a name="controltower-Type-LandingZoneOperationDetail-operationType"></a>
The landing zone operation type.
Valid values:
+  `DELETE`: The `DeleteLandingZone` operation.
+  `CREATE`: The `CreateLandingZone` operation.
+  `UPDATE`: The `UpdateLandingZone` operation.
+  `RESET`: The `ResetLandingZone` operation.
Type: String
Valid Values: `DELETE | CREATE | UPDATE | RESET`
Required: No

 ** startTime **   <a name="controltower-Type-LandingZoneOperationDetail-startTime"></a>
The landing zone operation start time.
Type: Timestamp
Required: No

 ** status **   <a name="controltower-Type-LandingZoneOperationDetail-status"></a>
Valid values:
+  `SUCCEEDED`: The landing zone operation succeeded.
+  `IN_PROGRESS`: The landing zone operation is in progress.
+  `FAILED`: The landing zone operation failed.
Type: String
Valid Values: `SUCCEEDED | FAILED | IN_PROGRESS`
Required: No

 ** statusMessage **   <a name="controltower-Type-LandingZoneOperationDetail-statusMessage"></a>
If the operation result is FAILED, this string contains a message explaining why the operation failed.
Type: String
Required: No

## See Also
<a name="API_LandingZoneOperationDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/controltower-2018-05-10/LandingZoneOperationDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/controltower-2018-05-10/LandingZoneOperationDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/controltower-2018-05-10/LandingZoneOperationDetail)
