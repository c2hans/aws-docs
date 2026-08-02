---
source_url: https://docs.aws.amazon.com/solutions/latest/clickstream-analytics-on-aws/user-identifier.html
---

# User identifier
<a name="user-identifier"></a>

 When you perform data analysis, you usually need to select an appropriate user identifier for analysis based on your business analysis scenario. This will help you improve the accuracy of your analysis, especially in funnel, retention, session and other analysis scenarios.

 Clickstream Analytics on AWS guidance mainly contains three types of IDs:
+  User ID
+  Device ID
+  User Pseudo ID

 This section introduces how to use these three IDs respectively, and you will learn in detail how to use User ID and User Pseudo ID to correlate user behavior.

## User ID
<a name="user-id"></a>

 User ID is usually a unique identifier that describes the user in your business database, which is relatively more accurate and unique.
+  When the user is not registered or logged in, the value of User ID is empty.
+  The SDK provides the ClickstreamAnalytics.setUserId("your user id") method to set the User ID. When logging out, set null/nil to clear the User ID.
+  The User ID is stored in the user\_id field in the user table.

## Device ID
<a name="device-id"></a>

 The guidance uses Device ID to identify user devices.
+  The Device ID will be automatically generated when the app is launched for the first time after integrating the SDK.
+  The Device ID may not be the unique identifier of the device. Usually the Device ID may be regenerated after the user uninstalls the app or clears the cache on the web page.
+  The Device ID is stored in the device\_id\_list field in the user table.

 The following table will introduce how the SDK on each end generates the Device ID.

|  **SDK Types**  |  **Generate Rules**  |  **Storage Location**  |  **Is Unique**  |
| --- | --- | --- | --- |
|  Android SDK  |  By default, AndroidId is used as the Device ID. If the AndroidId cannot be obtained, a random UUID is used instead  |  Stored in SharedPreference key-value pair file  |  Usually, the AndroidId will not change even if the app is uninstalled and reinstalled. If using the UUID as Device ID, it will change after the user uninstalls and reinstall the app  |
|  Swift SDK  |  If your app has been authorized to obtain IDFA, use IDFA as the Device ID. Otherwise, use IDFV as the Device ID. If IDFV cannot be obtained, use a random UUID  |  UserDefault key-value pair file  |  Usually, the IDFA does not change even if the app is uninstalled and reinstalled. When using IDFV or UUID, the Device ID will change after the user uninstalls and reinstalls the app  |
|  Web SDK  |  By default, a random UUID is used as the device ID  |  In the browser's localStorage  |  Device ID will be regenerated after user clears browser cache  |

## User Pseudo ID
<a name="user-pseudo-id"></a>

 Clickstream Analytics on AWS guidance uses User Pseudo ID to correlate logged-in and non-logged-in behavior on the same device.
+  User Pseudo IDs are generated from random UUIDs in all SDKs.
+  User Pseudo ID will only be reassigned when a new user logs in on the current device. When switching to a user who has already logged in on the current device, it will revert to the User Pseudo ID of the previous user.
+  The User Pseudo ID is stored in the user\_pseudo\_id field of the user table.

 The following table lists the correspondence between Device ID, User ID, and User Pseudo ID under various scenarios.

|  **Sequence**  |  **Events**  |  **Device ID**  |  **User ID**  |  **User Pseudo ID**  |
| --- | --- | --- | --- | --- |
|  1  |  Install App  |  S  |  --  |  1  |
|  2  |  Use the App  |  S  |  --  |  1  |
|  3  |  Logged in user A  |  S  |  A  |  1  |
|  4  |  Use the App  |  S  |  A  |  1  |
|  5  |  Sign out and view  |  S  |  --  |  1  |
|  6  |  Logged in user B  |  S  |  B  |  2  |
|  7  |  Use the App  |  S  |  B  |  2  |
|  8  |  Sign out and view  |  S  |  --  |  2  |
|  9  |  Logged in user A  |  S  |  A  |  1  |
|  10  |  Use the App  |  S  |  A  |  1  |
|  11  |  Sign out and view  |  S  |  --  |  1  |
|  12  |  Logged in user C  |  S  |  C  |  3  |
|  13  |  Use the App  |  S  |  C  |  3  |

 As shown in the table, you can count all the behavioral events of user A on device S when user A did not log in and after logging in twice by looking for user\_pseudo\_id=1. Additionally, you can use User ID to join user clickstream data with data from your business systems to build a more complete customer data platform.

**Note**
 When the user uninstalls the app or clears the browser cache, the relationship between the original User Pseudo ID and User ID will be cleared on the device, and a new User Pseudo ID will be generated on the device.
