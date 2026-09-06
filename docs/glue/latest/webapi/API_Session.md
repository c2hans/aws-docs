---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_Session.html
---

# Session
<a name="API_Session"></a>

The period in which a remote Spark runtime environment is running.

## Contents
<a name="API_Session_Contents"></a>

 ** Command **   <a name="Glue-Type-Session-Command"></a>
The command object.See SessionCommand.
Type: [SessionCommand](API_SessionCommand.md) object
Required: No

 ** CompletedOn **   <a name="Glue-Type-Session-CompletedOn"></a>
The date and time that this session is completed.
Type: Timestamp
Required: No

 ** Connections **   <a name="Glue-Type-Session-Connections"></a>
The number of connections used for the session.
Type: [ConnectionsList](API_ConnectionsList.md) object
Required: No

 ** CreatedOn **   <a name="Glue-Type-Session-CreatedOn"></a>
The time and date when the session was created.
Type: Timestamp
Required: No

 ** DefaultArguments **   <a name="Glue-Type-Session-DefaultArguments"></a>
A map array of key-value pairs. Max is 75 pairs.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 75 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[\.\-_A-Za-z0-9]+`
Value Length Constraints: Minimum length of 0. Maximum length of 4096.
Value Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** Description **   <a name="Glue-Type-Session-Description"></a>
The description of the session.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** DPUSeconds **   <a name="Glue-Type-Session-DPUSeconds"></a>
The DPUs consumed by the session (formula: ExecutionTime \* MaxCapacity).
Type: Double
Required: No

 ** ErrorMessage **   <a name="Glue-Type-Session-ErrorMessage"></a>
The error message displayed during the session.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** ExecutionTime **   <a name="Glue-Type-Session-ExecutionTime"></a>
The total time the session ran for.
Type: Double
Required: No

 ** GlueVersion **   <a name="Glue-Type-Session-GlueVersion"></a>
The AWS Glue version determines the versions of Apache Spark and Python that AWS Glue supports. The GlueVersion must be greater than 2.0.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^(\w+\.)+\w+$`
Required: No

 ** Id **   <a name="Glue-Type-Session-Id"></a>
The ID of the session.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** IdleTimeout **   <a name="Glue-Type-Session-IdleTimeout"></a>
The number of minutes when idle before the session times out.
Type: Integer
Required: No

 ** MaxCapacity **   <a name="Glue-Type-Session-MaxCapacity"></a>
The number of AWS Glue data processing units (DPUs) that can be allocated when the job runs. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB memory.
Type: Double
Required: No

 ** NumberOfWorkers **   <a name="Glue-Type-Session-NumberOfWorkers"></a>
The number of workers of a defined `WorkerType` to use for the session.
Type: Integer
Required: No

 ** ProfileName **   <a name="Glue-Type-Session-ProfileName"></a>
The name of an AWS Glue usage profile associated with the session.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** Progress **   <a name="Glue-Type-Session-Progress"></a>
The code execution progress of the session.
Type: Double
Required: No

 ** Role **   <a name="Glue-Type-Session-Role"></a>
The name or Amazon Resource Name (ARN) of the IAM role associated with the Session.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[^:]*:iam::[0-9]*:role/.+`
Required: No

 ** SecurityConfiguration **   <a name="Glue-Type-Session-SecurityConfiguration"></a>
The name of the SecurityConfiguration structure to be used with the session.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** Status **   <a name="Glue-Type-Session-Status"></a>
The session status.
Type: String
Valid Values: `PROVISIONING | READY | FAILED | TIMEOUT | STOPPING | STOPPED`
Required: No

 ** WorkerType **   <a name="Glue-Type-Session-WorkerType"></a>
The type of predefined worker that is allocated when a session runs. Accepts a value of `G.1X`, `G.2X`, `G.4X`, or `G.8X` for Spark sessions. Accepts the value `Z.2X` for Ray sessions.
Type: String
Valid Values: `Standard | G.1X | G.2X | G.025X | G.4X | G.8X | Z.2X`
Required: No

## See Also
<a name="API_Session_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/Session)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/Session)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/Session)
