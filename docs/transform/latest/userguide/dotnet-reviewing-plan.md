---
source_url: https://docs.aws.amazon.com/transform/latest/userguide/dotnet-reviewing-plan.html
---

# Reviewing your plan to prepare for transformation
<a name="dotnet-reviewing-plan"></a>

After [Confirming your repositories to prepare for transformation](dotnet-confirming-repos.md), and [Resolving package dependencies to prepare for transformation](dotnet-resolving-dependencies.md), the AWS account administrator must review the transformation plan and approve it in AWS Transform.

AWS Transform displays the job's list of repositories, dependent repositories, and dependent packages that were selected for transformation.

## Reviewing the transformation plan
<a name="reviewing-transformation-plan"></a>

AWS Transform displays the job's list of repositories, dependent repositories, and dependent packages that were selected for transformation.

**Note**
AWS Transform can transform a maximum of 100 dependencies and repositories per transformation plan.

1. If you are not the AWS account administrator, review the job plan, and if you accept it, select **Send for approval**.

1. If you are the AWS account administrator, you must review the plan, and when ready, approve the plan to start the transformation. After you review the job plan, select either:

   1. *Reject* If the job was created by a user who is not the AWS account administrator, we suggest you notify the job creator to restart the job.

   1. *Approve and start transformation*.

The job review includes the following details:

1. *Job summary* This includes:

   1. The target branch where AWS Transform will place the transformed code.

   1. The target .NET version, .NET 8.0 or .NET 10.

   1. The job settings:

      1. Exclude .NET standard projects

   1. Number of repositories selected for transformation

   1. Number of dependent repositories

   1. Number of private NuGet packages

   1. Total lines of code for the job

1. *Repositories selected* These are the repositories selected for transformation. They must be either MVC, Web, Windows Communication Foundation (WCF), Console, class library, UI framework - Razor pages, or unit test packages. This table includes the following information:

   1. Name

   1. Source branch

   1. Supported projects

   1. Lines of code

   1. Projects detected

   1. Projects skipped

   1. Dependencies detected

1. *Dependent repositories added* These are the dependent repositories added for transformation. They must be either MVC, Web, Windows Communication Foundation (WCF), Console, class library, UI framework - Razor pages, or unit test packages. This table includes the following information:

   1. Name

   1. Needed by

   1. Source branch

   1. Supported projects

   1. Lines of code

   1. Projects detected

   1. Projects skipped

1. *Dependent packages* These are the dependent packages added for transformation. They must be either MVC, Web, Windows Communication Foundation (WCF), Console, class library, UI framework - Razor pages, or unit test packages. This table includes the following information:

   1. Name

   1. Associated repositories

   1. Framework version status

   1. Core version status
