---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/gg-testing-framework.html
---

# Use AWS IoT Greengrass Testing Framework
<a name="gg-testing-framework"></a>

Greengrass Testing Framework (GTF) is a collection of building blocks that supports end-to-end automation from the customer perspective. GTF uses [Cucumber](https://cucumber.io) as the feature driver. AWS IoT Greengrass uses the same building blocks to qualify software changes on various devices. For more information, see [Greengrass Testing Framework on Github](https://github.com/aws-greengrass/aws-greengrass-testing/tree/dev_v1).

GTF is implemented using Cucumber, a tool used to run automated tests, to encourage a Behavior-Driven Development (BDD) of the components. In Cucumber, the features of this system are outlined in a special type of file called `feature`. Each feature is described in a human-readable format called scenarios which are specifications that can be converted into automated tests. Each scenario is outlined as a series of steps that define the interactions and outcomes of this system under test using a domain-specific language called Gherkin. A [Gherkin step](https://cucumber.io/docs/gherkin/reference/#steps) is linked to the programming code using a method called step definition which hard wires the specification to the test flow. Step definitions in GTF are implemented with Java.

**Topics**
+ [How it works](#gg-testing-framework-how-gtf-works)
+ [Changelog](#gtf-changelog)
+ [Greengrass Testing Framework configuration options](configuration-options-gtf.md)
+ [Tutorial: Run end-to-end tests using Greengrass Testing Framework and Greengrass Development Kit](run-e2e-tests-tutorial.md)
+ [Tutorial: Use a confidence test from the confidence test suite](confidence-tests-tutorial.md)

## How it works
<a name="gg-testing-framework-how-gtf-works"></a>

AWS IoT Greengrass distributes the GTF as a standalone JAR that consists of several Java modules. To use GTF for end-to-end testing of components, you must implement the tests within a Java project. Adding the testing standable JAR as a dependency in your Java project enables you to use the existing functionality of the GTF and extend it by writing your own custom test cases. To run the custom test cases, you can build your Java project and run the target JAR with the configuration options described in [Greengrass Testing Framework configuration options](configuration-options-gtf.md).

### GTF standalone JAR
<a name="w2ab1c24c19c25c11b5"></a>

Greengrass uses Cloudfront as a [Maven](https://maven.apache.org/) repository to host different versions of the GTF standalone JAR. For a full list of GTF versions, see [GTF releases](https://github.com/aws-greengrass/aws-greengrass-testing/releases).

GTF standalone JAR includes the following modules. It is not limited to only these modules. You can pick and choose each of these dependencies separately in your project or include all of them at once with the [testing standalone JAR file](https://github.com/aws-greengrass/aws-greengrass-testing/tree/dev_v1/aws-greengrass-testing-standalone).
+ `aws-greengrass-testing-resources`: This module provides abstraction for managing the lifecycle of an AWS resource during the course of a test. You can use this to define your custom AWS resources using `ResourceSpec` abstraction so GTF can take care of creation and removal of those resources for you.
+ `aws-greengrass-testing-platform`: This module provides platform-level abstraction for the device under test during the test lifecycle. It contains APIs used to interact with the OS independent of the platform and can be used to simulate the commands running in the device shell.
+ `aws-greengrass-testing-components`: This module consists of sample components that are used for testing the Greengrass core features such as deployments, IPC, and other features.
+ `aws-greengrass-testing-features`: This module consists of reusable common steps and their definitions which are used for testing within in the Greengrass environment.

**Topics**
+ [How it works](#gg-testing-framework-how-gtf-works)
+ [Changelog](#gtf-changelog)
+ [Greengrass Testing Framework configuration options](configuration-options-gtf.md)
+ [Tutorial: Run end-to-end tests using Greengrass Testing Framework and Greengrass Development Kit](run-e2e-tests-tutorial.md)
+ [Tutorial: Use a confidence test from the confidence test suite](confidence-tests-tutorial.md)

## Changelog
<a name="gtf-changelog"></a>

The following table describes the changes in each version of the GTF. For more information, see the [GTF Releases page](https://github.com/aws-greengrass/aws-greengrass-testing/releases) on GitHub.

|  **Version**  |  **Changes**  |
| --- | --- |
| 1.2.0 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/gg-testing-framework.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/gg-testing-framework.html)  |
| 1.1.0 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/greengrass/v2/developerguide/gg-testing-framework.html)  |
| 1.0.0 | Initial version. |
