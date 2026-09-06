---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/mainframe-decomposition-aws-transform/seeds.html
---

# Identifying seeds in legacy systems
<a name="seeds"></a>

When you work with mainframe legacy applications, you can use several key sources to help identify decomposition seeds. (For examples and a more comprehensive list of sources, see the table in this section.)
+ Naming conventions provide the first clue. For example, you can use program prefixes such as `PAYC` to indicate payroll-related functionality and `INV` to refer to invoice processing. You can decode job control language (JCL) job names into meaningful components to specify the domain, system, application, and functionality of the mainframe component.
+ Scheduler definitions provide another valuable perspective, especially for batch applications. They group related jobs together.
+ For online applications, customer information control system (CICS) transaction definitions reveal natural groupings. These definitions cluster related functionality together and create a logical starting point for decomposition.

Successful decomposition combines multiple approaches based on your specific needs and constraints. Start with a decomposition strategy or combination of strategies that best fits your modernization goal, and then identify seeds that align with the strategy.

Mainframe applications use naming standards to maintain the consistency, readability, and manageability of code, datasets, and resources. Standards vary across organizations, but they follow the common conventions in the following table so they can be used effectively as seed input.

|
|
| Convention | Definition | Length | Examples |
| --- |--- |--- |--- |
| Program names | Meaningful prefixes or suffixes that indicate the type or purpose of the mainframe (COBOL, PL/I, or Assembler) program. | 8 characters | + `PAYC0001` – payroll related<br />+ `INV0020` – invoice related |
| JCL job names | Prefixes to indicate the domain, system, application, and functionality of the mainframe component. | 8 characters | `RINPB001` might indicate:+ `R` – retail domain<br />+ `IN` – invoice<br />+ `P` – payment<br />+ `B` – batch<br />+ `001` – job ID |
| Job accounting parameters (job cards) | Job accounting information to group application components based on account code setup. | Depends on the source mainframe system | + `ACCFIN` – finance account <br />+ `ACCLED` – ledger account |
| Database tables | Prefixes or suffixes that represent the system or application. | 1-18 characters for IBM DB2 tables; 1-8 characters for IBM Information Management System Database Manager | + `INV_MATCH` – invoice matching<br />+ `CUST_MAST` – customer master |
| Scheduler files | Scheduler definition files.  Schedulers drive batch operations in legacy mainframe systems and can be used as decomposition seeds. When you use a CA Jobtrac scheduler, you can define jobs by using SCL files for each functionality. | 1-8 characters | + `pocreate.scl` – purchase order creation jobs<br />+ `invload.scl` – invoice loading jobs<br />+ `invmatch.scl` – invoice matching jobs<br />+ `trialbal.scl` – trial balance process jobs<br />+ `pymntpro.scl` – payment processing jobs |
| CICS transactions | CICS system definition (CSD) files for online applications. You can use CSD files to group modules based on transaction group definitions. | 1-4 characters | In the following definitions, two transactions (`CAUP`, `CAVW`) and one online CICS program (`COACTVWC`) are included in the `ACCTMGNT` (account management) group:<pre>DEFINE TRANSACTION(CAUP) GROUP(ACCTMGNT)<br />DEFINE PROGRAM(COACTVWC) GROUP(ACCTMGNT)<br />DEFINE TRANSACTION(CAVW) GROUP(ACCTMGNT)</pre> |

Other decomposition grouping options include file names (datasets) and copybook file members, if these components follow meaningful naming standards.
