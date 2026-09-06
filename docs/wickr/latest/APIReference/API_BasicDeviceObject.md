---
source_url: https://docs.aws.amazon.com/wickr/latest/APIReference/API_BasicDeviceObject.html
---

# BasicDeviceObject
<a name="API_BasicDeviceObject"></a>

Represents a device where a user has logged into Wickr, containing information about the device's type, status, and login history.

## Contents
<a name="API_BasicDeviceObject_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** appId **   <a name="wickr-Type-BasicDeviceObject-appId"></a>
The unique application ID for the Wickr app on this device.
Type: String
Pattern: `[\S\s]*`
Required: No

 ** created **   <a name="wickr-Type-BasicDeviceObject-created"></a>
The timestamp when the device first appeared in the Wickr database.
Type: String
Pattern: `[\S\s]*`
Required: No

 ** lastLogin **   <a name="wickr-Type-BasicDeviceObject-lastLogin"></a>
The timestamp when the device last successfully logged into Wickr. This is also used to determine SSO idle time.
Type: String
Pattern: `[\S\s]*`
Required: No

 ** statusText **   <a name="wickr-Type-BasicDeviceObject-statusText"></a>
The current status of the device, either 'Active' or 'Reset' depending on whether the device is currently active or has been marked for reset.
Type: String
Pattern: `[\S\s]*`
Required: No

 ** suspend **   <a name="wickr-Type-BasicDeviceObject-suspend"></a>
Indicates whether the device is suspended.
Type: Boolean
Required: No

 ** type **   <a name="wickr-Type-BasicDeviceObject-type"></a>
The operating system of the device (e.g., 'MacOSX', 'Windows', 'iOS', 'Android').
Type: String
Pattern: `[\S\s]*`
Required: No

## See Also
<a name="API_BasicDeviceObject_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wickr-2024-02-01/BasicDeviceObject)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wickr-2024-02-01/BasicDeviceObject)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wickr-2024-02-01/BasicDeviceObject)
