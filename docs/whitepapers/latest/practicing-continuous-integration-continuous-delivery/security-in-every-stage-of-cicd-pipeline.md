---
source_url: https://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/security-in-every-stage-of-cicd-pipeline.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Security in every stage of CI/CD pipeline
<a name="security-in-every-stage-of-cicd-pipeline"></a>

 Security must be applied to every component of the infrastructure, including CI/CD pipelines, from the moment a single line of code is written to the stages where it's deployed. That deployment can include multiple environments, identities, systems, and any applications which interact with it. During its journey, it's modified and updated continuously. The following image shows different stages of a typical CI/CD pipeline.

![Diagram depicting CI/CD](https://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/images/cicd1.png)

 Due to the nature of continuous integration, every change needs to be monitored and made sure that it's safe to release towards the environment you are building. For every stage, there are multiple controls that can be embedded to the process whereas tool integrations are not sufficient by themselves for a secure CI/CD pipeline. From the people, process and technology perspective:
+  People delivering, handling and monitoring the code must have the awareness towards secure coding practices. They should stick to these guidelines and must never abandon them to deliver faster.
+  Processes must be defined and reiterated continuously to make sure that your level of security is consistent across each and every stage of the pipeline.
+  Technologies must be implemented to support the process mentioned above in each and every stage and must never be circumvented.

 Security checks must be applied throughout the build process which will stop the process if a security concern exists. The following is a sample of some technologies that can be integrated throughout the CI/CD pipeline. Review the [Deployment Pipeline Reference Architecture](https://pipelines.devops.aws.dev/) for a more complete list.

![Detailed diagram of Deployment Pipeline Reference Architecture](https://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/images/cicd2.png)

 Security is a shared responsibility between AWS and customers. Refer to the security [documentation](https://docs.aws.amazon.com/codecatalyst/latest/userguide/security.html) to understand how to apply the shared responsibility model when using Amazon CodeCatalyst.

## Pre-commit hooks
<a name="pre-commit-hooks"></a>

 Pre-commit hooks are pieces of code or scripts that are run at the developer’s environment (workstation, CodeCatalyst Dev Environments, AWS Cloud9, or any other environment where code is developed) before a change to code is committed to the pipeline. Hooks are controls that can be configured per general practices or company policies and any code update that is not compliant against those policies are blocked till they are corrected.

## IDE tools and plugins
<a name="ide-tools-and-plugins"></a>

 Integrated Development Environment (IDE) is the tool which most developers use to write their code. IDEs bring convenience to the developers with built-in or deployable plugins which can walk through the code including but not limited to detecting potential issues, giving recommendations for improvements, linting, formatting, beautifying and securing it.

## Static Application Security Testing (SAST)
<a name="static-application-security-testing-sast"></a>

 SAST also known as static analysis or static code analysis are tools that detect bugs by analyzing the source code. SAST tools are built with the general approach of working backwards by dissecting the vulnerabilities to define possible attack methodologies and generate signatures against them to act as a preventative measure.

## Software Composition Analysis (SCA)
<a name="software-composition-analysis-sca"></a>

 SCA is an automated process to identify the open-source packages that are in use within the code to define vulnerabilities and potential compliance-based issues. SCA tools identify open-source packages in an application and all the vulnerabilities that are present in them. They can also check the licenses for each package, check dependencies and bring infrastructure as code (IaC) manifests for potential vulnerabilities in containerized environments.

## Dynamic Application Security Testing (DAST)
<a name="dynamic-application-security-testing-dast"></a>

 DAST tools also named as black-box solutions, test the applications during the lifecycle of their operations and give recommendations towards potential vulnerabilities and compliance issues. Since they monitor the behavior of the applications, they tend to generate less false positives compared to SAST tools.

## Interactive Application Security Testing (IAST)
<a name="interactive-application-security-testing-iast"></a>

 IAST tools are a combination of SAST and DAST tools and embody both tools’ advantages within. They are usually facilitated during the test and QA stages since it is the closest version of the production-level code. While running dynamically to identify the issues like a DAST tool, it will also be run inside the application server to evaluate the code like a SAST tool. The findings are real-time and IAST tools are also useful for API testing.

## Penetration testing
<a name="penetration-testing"></a>

 Penetration testing aims to make sure that no vulnerability or non-compliant assets go unnoticed towards the end-product. Both tool and human based penetration testing methodologies are used towards applications and both have their benefits towards detecting vulnerabilities. Penetration testing should be done with a multi-directional approach while traversing the application to monitor and detect possible different behaviors of the application and user experiences.

## Red/Blue/Purple teaming
<a name="redbluepurple-teaming"></a>

 Red/Blue/Purple teams are security experts with different roles to simulate real-life cyber-attacks. Their aim is to pinpoint system deficits, improve protection mechanisms and processes, and maximize the efficiency of the infrastructure while minimizing the risk. Red teams represent the attackers, blue teams operate as defenders, and purple teams include members from both teams to fulfill a multi-faceted approach and bring various perspectives for security.
