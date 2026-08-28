---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2022-06-29-windows-pv-retire.html
---

# Release: Elastic Beanstalk Windows Server platform versions V0 and V1 retired on June 29, 2022
<a name="release-2022-06-29-windows-pv-retire"></a>

This release announces the retirement of the remainder of the Windows Server platform versions for version 0.1.0 and version 1.2.0.

**Release date:** June 29, 2022

## Changes
<a name="release-2022-06-29-windows-pv-retire.changes"></a>

Today we're announcing the retirement of the remainder of the Windows Server platform versions for **version 0.1.0** and **version 1.2.0**.

**Note**
 The vast majority of Elastic Beanstalk customers that use the Windows Server platforms use the **version 2.x** platform versions and will not be affected by this retirement.

*The following platform versions are now retired.*
+ IIS 8 running on 64bit Windows Server 2012 R1 *version 0.1.0*
+ IIS 8 running on 64bit Windows Server 2012 R1 *version 1.2.0*
+ IIS 8.5 running on 64bit Windows Server 2012 R2 *version 0.1.0*
+ IIS 8.5 running on 64bit Windows Server 2012 R2 *version 1.2.0*
+ IIS 8.5 running on 64bit Windows Server Core 2012 R2 *version 0.1.0*
+ IIS 8.5 running on 64bit Windows Server Core 2012 R2 *version 1.2.0*
+ IIS 10.0 running on 64bit Windows Server 2016 *version 1.2.0*
+ IIS 10.0 running on 64bit Windows Server Core 2016 *version 1.2.0*

If you currently use any of these retired platform versions, we strongly recommend that you migrate to one of the Windows Server **version 2.x** platform versions, which are current and fully supported. For a list of these platform versions, see [Supported Platforms](https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platforms-supported.html#platforms-supported.net) in the *AWS Elastic Beanstalk Platforms* guide. For full migration considerations, see [Major Version Migration](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/dotnet-v2migration.html) in the *AWS Elastic Beanstalk Developer Guide*.

For more information and a listing of retired platform components, see [Elastic Beanstalk platform support policy](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/platforms-support-policy.html) in the *AWS Elastic Beanstalk Developer Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Beanstalk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticbeanstalk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
