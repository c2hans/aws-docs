---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/iap-on-aws/service-catalog-puppet.html
---

# Service Catalog Puppet
<a name="service-catalog-puppet"></a>

Service Catalog Puppet is implemented in Python by using the AWS Boto3 API. This tool offers several powerful features for configuring and provisioning Service Catalog products. Developers can configure Service Catalog product and portfolio provisioning information by using YAML templates that serve as manifests. Service Catalog Puppet provisioning workflows support products that require more complex deployment processes than Service Catalog. They also support performance optimizations to provision products at scale within aggressive time windows.

Service Catalog Puppet accesses the Service Catalog CloudFormation templates for product provisioning at deployment time. It calls CloudFormation directly to deploy the provisioning template stack for a product and bypasses the restrictions imposed by Service Catalog's own stack set provisioning process. If the provisioning template uses macros to include other CloudFormation scripts or uses nested CloudFormation scripts, you must provide access to those scripts in the target account in the bootstrapping portion of the provisioning workflow.

For more information:
+ See the Service Catalog Puppet [documentation](https://service-catalog-tools-workshop.com/tools/puppet.html) and [GitHub repository](https://github.com/awslabs/aws-service-catalog-puppet).
+ If you want to use the Service Catalog Puppet SDK to interact with the tool programmatically to initiate product and portfolio provisioning, see the [SDK documentation](https://aws-service-catalog-puppet.readthedocs.io/en/latest/puppet/using_the_sdk.html).
+ [GitOps](https://service-catalog-tools-workshop.com/managing-your-environments/gitops.html) is the default mechanism for managing the Service Catalog Puppet environment.

Service Catalog Puppet is fairly easy for developers to learn. It requires familiarity with AWS CloudFormation to implement product provisioning templates and YAML templates to implement manifests. There are good workshops available to bring new developers up to speed, such as [self-paced workshops](https://service-catalog-tools-workshop.com/2021-workshop.html).

## Support for provisioning workflows
<a name="provisioning-workflow-support"></a>

Service Catalog Puppet employs the Python Luigi task orchestration engine to implement bootstrapping and provisioning workflows. All steps in these workflows are implemented as Luigi workflow tasks. For an overview of Luigi and how it compares to other popular workflow tools, see [Airflow vs. Luigi vs. Argo vs. MLFlow vs. KubeFlow](https://www.datarevenue.com/en-blog/airflow-vs-luigi-vs-argo-vs-mlflow-vs-kubeflow) on the Data Revenue blog.

Luigi allows Service Catalog Puppet to control the number of workers associated with workflow tasks, and to control other aspects of the workflows, for better scaling and performance.

Service Catalog Puppet also provides a [depends\_on](https://service-catalog-tools-workshop.com/managing-your-environments/fine-grained-depends-on.html) mechanism for managing product and step dependencies, and for orchestrating product provisioning. This feature helps you implement and operationally manage fine-grained product definitions and complex dependencies.

## Provisioning modes
<a name="provisioning-modes"></a>

Service Catalog Puppet supports three execution modes: [hub, async, and spoke](https://aws-service-catalog-puppet.readthedocs.io/en/latest/puppet/execution_modes.html). All three modes provision products within portfolios that are already defined in Service Catalog.  They rely on Service Catalog product sharing to the target accounts and use Service Catalog administrator and launch roles to realize provisioning in those targets. Service Catalog Puppet performs the bootstrapping steps within the same organization based on the role configurations provided in the YAML configuration files. The tool also supports provisioning to multiple organizations from a single hub account. In this scenario, bootstrapping must be performed manually in the external organizations to allow Service Catalog Puppet to perform required provisioning actions in the external organization's accounts.

In all provisioning modes, Service Catalog Puppet implements product provisioning directly without calling Service Catalog's provisioning process. You can configure a provisioning manifest to use the role and target account specifications in an existing Service Catalog stack set constraint. Service Catalog Puppet uses this information to do its own provisioning with Luigi workflows.

You can define targets for product portfolio provisioning based on an account tagging approach, in addition to specifying OUs or accounts directly. In account tag-based provisioning, a portfolio product is provisioned to all accounts that have all the tags in the specified manifest provisioning tag set. For example, if you want to issue a portfolio product to all institutional production accounts in US East Regions, you could specify the tags `type:prod`, `partition:us-east`, and `scope:institutional-client`. You can also declare account and OU exclusions to prohibit provisioning to OUs or accounts that have the tags that you specify, or to accounts that are members of the OU-specified targets. For more information about account tagging, see the [Service Catalog Tools documentation](https://service-catalog-tools-workshop.com/design-considerations/account-tagging.html).

**Hub mode**

In hub provisioning mode, all Luigi workflows for the spoke accounts are managed from the designated central hub account. The hub account assumes an IAM role that allows it to perform actions in a spoke account, but the management of tasks occurs from within the hub account. The hub account waits synchronously until all spoke account provisioning tasks complete, either successfully or unsuccessfully. It then reports final status. The hub account mode is the oldest and most mature provisioning mode. However, many users have moved to the spoke provisioning mode to achieve greater provisioning concurrency and speed.

**Spoke mode**

In spoke mode, the Service Catalog hub account initiates the Luigi workflows to run in the designated bootstrapped spoke accounts. The hub account is notified when the spoke workflows complete. Failures in a spoke account rise up to the hub account. The hub account polls the spoke account to see if it's finished and to determine status.

Spoke mode is least likely to require AWS service quota increases because almost everything runs in the separate spoke accounts. Spoke mode also provides far greater concurrency than hub mode while retaining central control. It can improve provisioning speed by 800 percent over hub mode. Spoke mode supports product chaining through DependsOn relationships between products, which ensures that a product that is depended on has already been provisioned. A product that comprises chained products can also provision a component chained product. You can also use specialized AWS Lambda function calls to perform required steps. Faults in one spoke are isolated from other spokes.

Spoke mode is used by enterprises that have over 980 accounts in up to 7 Regions. These enterprises are generally able to provision a product to all Regions and accounts in their infrastructure within an hour.

**Note**
These results might vary based on factors such as the networking infrastructure, the workload, and the quotas in place for the AWS organization hub and spoke accounts. They also depend on the product resources that are being provisioned, their inherent creation times, and their dependencies on other resources.

**Async mode**

Async mode initiates provisioning workflows in spoke accounts, but it doesn't wait for or receive completion responses from the spokes.

## Caching
<a name="learning-sc-puppet"></a>

Another mechanism that Service Catalog Puppet uses to optimize the speed of workflows is to cache common tasks that represent steps in the workflow. When a cached task is complete, it writes its output to Amazon Simple Storage Service (Amazon S3). The next time the task is invoked in the same session with the same parameters, Service Catalog Puppet uses the cached values instead of rerunning the task. For more information, see [Caching](https://aws-service-catalog-puppet.readthedocs.io/en/latest/puppet/caching.html) in the Service Catalog Puppet documentation.SC Puppet is fairly easy for developers to learn and only requires an understanding of CloudFormation to implement SC Product provisioning templates and YAML templates to implement SC Puppet manifests. The learning curve is fairly low and there are good workshops already available to bring new developers up to speed on SC Puppet.

## SDLC DevSecOps support
<a name="sdlc-dev-sec-ops-support"></a>

Service Catalog Puppet includes support for managing the DevSecOps pipeline. You can use Service Catalog Tools actions (as illustrated in the [Service Catalog Puppet overview](https://service-catalog-tools-workshop.com/tools/puppet.html))

to automate testing and to promote products across your AWS lifecycle accounts, including the recommended canary account. For more information, see [Managing your environments](https://service-catalog-tools-workshop.com/managing-your-environments.html) in the Service Catalog Puppet documentation.

To ensure that any issues related to a product change are detected before widespread production use, Service Catalog Puppet requires at least one canary account for initial deployment. After you test and gain confidence in the new release, you can promote it to non-canary production accounts. If you identify any issues, you can roll the release back and reintroduce it when the issues are resolved. When you use this approach, production issues might occur if you release a canary version that has an issue to production accounts. As an alternative approach, you can run full regression tests for each product change before releasing the change to production. This introduces additional overhead in the CI/CD process but helps avoid production issues. It is the DevSecOps administrator's responsibility to determine the best feature release scenarios and approaches for their development teams.

Service Catalog Puppet allows multiple teams to develop and test the provisioning of Service Catalog product solutions simultaneously. As a best practice, a product shouldn't be changed by multiple developers at the same time. Instead, you can break out products into finer-grained components for separate, simultaneous modifications.

Service Catalog Puppet also helps automate testing through an assertion statement that provides static and unit test capabilities. You can test service control policies (SCPs) and IAM policies by using policy simulators. These are technically end-to-end tests but can be used in system integration test (SIT) environments. For more information, see [Using policy simulations](https://service-catalog-tools-workshop.com/every-day-use/680-using-policy-simulations.html) and [Applying service control policies](https://service-catalog-tools-workshop.com/every-day-use/800-applying-service-control-policies.html) in the Service Catalog Puppet documentation.

## Maturity, completeness, and support
<a name="maturity-completeness-support"></a>

Although Service Catalog Puppet isn't an officially supported AWS service, it has been widely adopted. This tool has been used by large organizations over the last few years to successfully and centrally provision products to hundreds of OU accounts within their desired provisioning time windows. It has proven to provide fault-tolerant product provisioning at scale. Users who encounter any issues with Service Catalog Puppet can log them in the [GitHub repository](https://github.com/awslabs/aws-service-catalog-puppet) for resolution by the contributors to this AWS Labs solution.
