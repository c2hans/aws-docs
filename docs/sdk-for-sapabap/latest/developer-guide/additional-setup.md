---
source_url: https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/additional-setup.html
---

# Refresh, trace, and telemetry topics for AWS SDK for SAP ABAP
<a name="additional-setup"></a>

This section covers the following topics.

**Topics**
+ [SAP system refresh](#refresh)
+ [Trace](#trace)
+ [Telemetry](#telemetry)

## SAP system refresh
<a name="refresh"></a>

After a system refresh, the primary challenge for a Basis administrator is to ensure that the separate systems are not accessing each other’s resources. For example, you may want to ensure that your QA SAP system is not accessing the resources, such as an S3 bucket, of your Production landscape.

SDK for SAP ABAP provides a safety-conscious approach of *logical resources* to this challenge. A business analyst can take the following steps.

1. Define a logical resource, such as `ZINVOICE_OUTBOUND`.

1. Map all systems and clients in the development system.

1. Transport the configuration of ALL systems forward until the production landscape.

**Basis steps after a refresh**

1. Check the authentication
+ If the system is using Secret Access Key authentication, the SSF-encrypted credentials will be invalid because they are stored in master data. The credentials must be re-entered, which may require regenerating a new Secret Access Key in [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).
+ If the system is authenticating with EC2 instance metadata, no steps are required.

Check the trace settings
+ In `/AWS1/IMG`, ensure that the trace settings are what you want. These settings are not transportable.

## Trace
<a name="trace"></a>

Trace output is controlled in the **IMG runtime settings**.

 The trace levels that you can use are:
+ **No Trace**
+ **Trace API calls**
+ **Trace API calls and payload**

  *This option contains unencrypted payload information.*
+ **Trace API calls, payload, and internal XML transformation**

  *This option contains unencrypted payload information.*

If API trace is activated, traces are written to `DIR_WORK` in `aws1_trace-{{YYYY-MM-DD}}.log` file.

If payload trace is additionally activated, additional files with the title `aws1_payload_*` are created for each call and payload component. The payload trace length can be limited with the length limit applying to each individual payload trace fail.

Payload traces are primarily intended to collect information to be provided to Support in the event of a serialization error. We recommend that you choose **No Trace** unless you're attempting to diagnose an SDK error.

**Note**
Payload traces can contain unencrypted business information. We recommend turning these traces on only for a request by AWS Support to help you troubleshoot. You can turn these traces off after resolution. Traces are not automatically deleted, and need to be removed by the system administrator when no longer needed.

These settings are not applicable to SDK for SAP ABAP - BTP edition.

## Telemetry
<a name="telemetry"></a>

SDKs send telemetry information to Support. SDK for SAP ABAP collects the following information:
+ OS release and patch level
+ `SAP_BASIS` release and patch level
+ SAP Kernel release and patch level

You can opt in to send the following information to Support.
+ SAP SID and instance name (`host_sid_nn`)
+ SAP Client (`SY-MANDT`)
+ Transaction code (`SY-TCODE`) and report (`SY-REPID`)

The additional information enables Support to help you better. Support can detect why a certain API call was made and can further find the relevant transaction in a SAP system.

Telemetry is limited to the SDK and API versions for SDK for SAP ABAP - BTP edition.
