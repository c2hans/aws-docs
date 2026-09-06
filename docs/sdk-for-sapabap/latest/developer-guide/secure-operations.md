---
source_url: https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/secure-operations.html
---

# Secure operations
<a name="secure-operations"></a>

## Encryption Of Data At Rest
<a name="rest"></a>

AWS Secret Access Keys are used for authenticating the SDK. They are encrypted using the SSF or Credential Store functionality by SAP.

## Encryption Of Data In Transit
<a name="transit"></a>

All calls to AWS services are encrypted with HTTPS. The SAP ICM manages the HTTPS connection. AWS certificates must be trusted in STRUST.

## API Usage
<a name="api"></a>

 When an ABAP user assumes a role using `sts:assumeRole`, the session name is titled `USERID-SID-MANDT`, where:
+ `USERID` is the ABAP user from `SY-UNAME` variable.
+ `SID` is the ABAP system ID from `SY-SYSID` variable.
+ `MANDT` is the ABAP client from `SY-MANDT` variable.

The session name appears in CloudTrail as *user name*. This ensures that API calls from an ABAP user can be traced back to the system, client, and user that initiated the call. For more information, see [What is AWS CloudTrail?](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html)
