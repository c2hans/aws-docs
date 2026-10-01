---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/ivr-design-on-connect/introduction.html
---

# Designing the foundation of a dynamic and modular IVR experience on Connect Customer
<a name="introduction"></a>

*Ayesha Borker and Nicholas Pung, Amazon Web Services*

Technical architects, developers, and business teams have the opportunity to reimagine the automated self-service experiences they offer to their customers when they migrate to a cloud-based contact center by using Amazon Connect Customer.

Business teams typically want to add functionality and features while making the self-service experience more personalized. Technical architects and developers focus primarily on how to reduce redundancy, enable rapid change and flexibility, modularize repeated processes, and decrease the maintenance overhead.

This guide provides technical architects with a set of best practices they can use to create the foundational design of their interactive voice response (IVR) application in a modular and dynamic fashion. It provides examples of IVR systems (that is, voice technologies). However, you can extend the same concepts to any other channels. The guide focuses on creating a modular and scalable IVR design by using Connect Customer flows and modules. Amazon Lex V2, which enables you to add natural language (NL) features to your IVR application, is out of scope.

## Overview
<a name="overview"></a>

Traditional methods for IVR experience design can be static and complex. Organizations often manage separate experiences for different languages, deployment environments (such as development, testing, and production), countries, and lines of business (LOBs). They frequently rely on human voice talent to create prompts, which are then uploaded and referenced in hard-coded scripts. This complicates the process for making changes and updates, especially in real time for emergencies or time-sensitive announcements. When applications are separated in this manner, we often observe that common use cases are repeated and are managed redundantly. Common examples include the intake of payments on an IVR system or sending a post-transaction SMS. Backend integrations to databases, customer relationship management (CRM) solutions, or other third-party systems are often hard-coded, which means that changes have to be manually replicated across multiple applications.

This type of a monolithic architecture design leads to excessive administrative processes and management overhead, and impedes innovation. Developers spend more time implementing small changes across multiple dependencies, which makes it difficult for them to follow agile processes. Often, this complexity becomes burdensome and companies must rely on professional services organizations or external consultants to help manage these changes. As a result, the business experiences increased turnaround time for typical updates. A complicated architecture that involves these complex and time-consuming development cycles results in increased cost.

This guide focuses on a foundational architecture for an IVR application that helps eliminate redundancies and streamlines the change management process. This architecture makes it easy for developers to maintain and innovate, and also provides businesses with the agility they need.
