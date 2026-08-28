---
source_url: https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-arc-zonal-shift.html
---

# Amazon Application Recovery Controller (ARC) in AWS GovCloud (US)
<a name="govcloud-arc-zonal-shift"></a>

 Amazon Application Recovery Controller (ARC) (ARC) provides capabilities that help you prepare for and accomplish faster recovery operations for applications running on AWS. With ARC, you can gain insights into whether your applications and resources are prepared for recovery, and quickly mitigate impairments for a multi-Availability Zone or multi-Region application. ARC includes readiness checks, routing controls, zonal shifts, and zonal autoshift.

## Region availability
<a name="_region_availability"></a>

This service is available in the following AWS GovCloud (US) Regions:
+  AWS GovCloud (US-West)
+  AWS GovCloud (US-East)

## How Amazon Application Recovery Controller (ARC) differs
<a name="_how_amazon_application_recovery_controller_arc_differs"></a>

The following differences apply to Amazon Application Recovery Controller (ARC):
+ The routing control, and readiness check features of the ARC service are not available in AWS GovCloud (US-West).

## Zonal Shift
<a name="_zonal_shift"></a>

You can use ARC zonal shift to quickly isolate and recover from single Availability Zone (AZ) impairments. Zonal shift temporarily shifts traffic for a supported resource away from an impaired AZ to healthy AZs in the same AWS Region. Starting a zonal shift helps your application recover quickly, for example, from a developer’s bad code deployment or from an AWS impairment in a single AZ. Shifting traffic away from the impaired AZ reduces the impact for clients who are using your application in the impaired AZ.

You can start a zonal shift for any supported resource in your account in an AWS Region. Zonal shifts are manual and temporary. When you start a zonal shift, you must specify an (extendable) expiration of up to three days.

## Region Switch
<a name="_region_switch"></a>

You can use Region switch in ARC to orchestrate large-scale, complex recovery tasks for your application resources across AWS accounts, to help ensure business continuity and reduce operational overhead. Region switch provides a centralized and observable solution that you can perform manually, or automate by using Amazon CloudWatch alarm triggers. If an AWS Region becomes impaired, you can execute the plans that you create by using Region switch to fail over or switch your resources to another Region. This ensures that your application can continue to operate, running in a healthy AWS Region.

## Documentation
<a name="govcloud-docs-83"></a>
+  [Amazon Application Recovery Controller Developer Guide﻿](https://docs.aws.amazon.com/r53recovery/latest/dg/what-is-route53-recovery.html)

## Export-controlled content
<a name="govcloud-itar-content-122"></a>

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.
+ All customer parameters provided as input to ARC through the console, APIs, or other mechanisms, are not permitted to contain export-controlled data. Examples include comments entered by the user, and the resource name and Amazon Resource Name (ARN) for registered resources.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS GovCloud (US). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query govcloud-us` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
