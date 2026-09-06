---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/replatform-mainframe-apps-shared-db2/build.html
---

# Building
<a name="build"></a>

Using a shared Db2 database enables concurrent execution of identical or consistent applications in both mainframe and cloud environments. This approach offers several advantages when you maintain the same application version across both platforms, and provides enhanced flexibility and reliability in your operations.

One key advantage of this strategy is the ability to implement an effective rollback plan. If issues arise during migration or deployment, having the same application version allows for a seamless reversion to the previous state, and minimizes downtime and potential data inconsistencies.

## Application consistency
<a name="mirroring"></a>

Mirroring application components from a distributed source control manager to the mainframe is a strategic approach during the replatforming process. This method supports the use of modern source code management tools while maintaining synchronization with the mainframe environment. This mirroring process is temporary, and lasts only until the workload is fully functional in production on the distributed platform.

By migrating your replatformed application's source code to a distributed change management tool, you can take advantage of several benefits offered by modern source code managers. These include:
+ **Enhanced collaboration**: Distributed tools often provide better support for team collaboration by including features such as pull requests, code reviews, and branching strategies.
+ **Improved version control**: Modern systems offer more granular version control, and make it easier to track changes and manage different versions of the code.
+ **Integration with CI/CD pipelines**: Many distributed tools seamlessly integrate with continuous integration and continuous deployment (CI/CD) pipelines, which streamline the development process.
+ **Better visibility and traceability**: These tools often provide superior dashboards and reporting capabilities, and offer greater insight into the development process.
+ **Support for modern development practices**: Distributed systems are typically better suited for agile methodologies and DevOps practices.

The mirroring process involves synchronizing the code from the distributed source control manager back to the mainframe. This ensures that both environments remain consistent during the transition period. However, you must implement mirroring as a one-way synchronization, where updates flow from the distributed system to the mainframe, instead of bidirectionally. This approach maintains consistency and prevents potential conflicts that could arise from simultaneous updates in both environments.

By adopting this mirroring strategy, you can gradually shift your development efforts to the distributed platform while ensuring that the mainframe environment remains up-to-date. This provides a smoother transition and a safety net during the replatforming process. When the workload is fully functional and stable in the distributed production environment, you can phase out the mirroring process and complete the migration to the modern source code management system.

## Architecture
<a name="planning-architecture"></a>

The following diagram shows how a distributed source code management system can mirror application components and maintain synchronization between the AWS Cloud and mainframe environments. The AWS Cloud environment uses CI/CD services such as [AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html), [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html), and [AWS CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/welcome.html) to build and deploy the application.

![Architecture for gradual mainframe migration with application mirroring.](http://docs.aws.amazon.com/prescriptive-guidance/latest/replatform-mainframe-apps-shared-db2/images/guide-img/b5c7b078-cfe6-46c4-b120-94b5824d3c88/images/6df9f2ab-5d88-4826-9188-9c6b855e6521.png)

In this workflow:

1. The application owners deliver a new application release into the development branch of the source code repository.

1. The new release triggers AWS CodePipeline.

1. AWS CodeBuild retrieves Db2 credentials from [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html).

1. CodeBuild compiles the application.

1. CodeBuild uses Db2 for z/OS to bind the application.

1. The mainframe delivery flow builds and deploys the application as well.
