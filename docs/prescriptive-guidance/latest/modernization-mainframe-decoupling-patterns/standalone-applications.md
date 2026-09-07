---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-mainframe-decoupling-patterns/standalone-applications.html
---

# Standalone applications
<a name="standalone-applications"></a>

In the following diagram, applications A and B are standalone mainframe applications. Each application consists of programs and subprograms that it uses exclusively.

![Applications A and B.](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-mainframe-decoupling-patterns/images/guide-img/a6175648-8ce0-4ab7-9a68-cebf41995535/images/8d9175ee-6a26-45f9-83e8-486e8db06974.png)

**Note**
For simplicity, all the diagrams in this guide illustrate programs that are shared by two applications, and subprograms that are called by two programs. In a complex mainframe application, a program might be called by many applications, and subprograms might be called by many programs.

Because the applications are self-contained, you can group the COBOL programs and subprograms by application for code refactoring, as shown in the following diagram.

![Group the COBOL programs and subprograms by application for code refactoring.](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-mainframe-decoupling-patterns/images/guide-img/a6175648-8ce0-4ab7-9a68-cebf41995535/images/38c06f75-44ec-43f5-8a80-782dccb5d577.png)

After grouping, you can migrate applications A and B in the same wave or in different waves. In either case, follow these steps:

1. For each application, package the refactored modern components and deploy them together into a runtime environment.

1. After migration, retire the on-premises mainframe applications and their components.
