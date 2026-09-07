---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/transfer-large-scale-db2-z-os-data-to-amazon-s3-in-csv-files.html
---

# Transfer large-scale Db2 z/OS data to Amazon S3 in CSV files
<a name="transfer-large-scale-db2-z-os-data-to-amazon-s3-in-csv-files"></a>

*Bruno Sahinoglu, Abhijit Kshirsagar, and Ivan Schuster, Amazon Web Services*

## Summary
<a name="transfer-large-scale-db2-z-os-data-to-amazon-s3-in-csv-files-summary"></a>

A mainframe is still a system of record in many enterprises, containing a massive amount of data including master data entities with records of current as well as the historical business transactions. It is often siloed and not easily accessed by the distributed systems within the same enterprise. With the emergence of cloud technology and big data democratization, enterprises are interested in using the insights hidden in the mainframe data to develop new business capabilities.

With that objective, enterprises are looking to open their mainframe Db2 data to their Amazon Web Services (AWS) Cloud environment. The business reasons are several and the transfer methods differ from case to case. You might prefer to connect your application directly to the mainframe, or you might prefer to replicate your data in near real time. If the use case is to feed a data warehouse or a data lake, having an up-to-date copy is no longer a concern, and the procedure described in this pattern might suffice, especially if you want to avoid any third-party product licensing costs. Another use case might be the mainframe data transfer for a migration project. In a migration scenario, data is required for performing the functional equivalence testing. The approach described in this post is a cost effective way to transfer the Db2 data to the AWS Cloud environment.

Because Amazon Simple Storage Service (Amazon S3) is one of the most integrated AWS services, you can access the data from there and gather insights directly by using other AWS services such as Amazon Athena, AWS Lambda functions, or Amazon QuickSight . You can also load the data to Amazon Aurora or Amazon DynamoDB by using AWS Glue or AWS Database Migration Service (AWS DMS). With that aim in mind, this describes how to unload Db2 data in CSV files in ASCII format on the mainframe and transfer the files to Amazon S3.

For this purpose, [mainframe scripts](https://github.com/aws-samples/unloaddb2-samples) have been developed to help to generate job control languages (JCLs) to unload and transfer as many Db2 tables as you need.

## Prerequisites and limitations
<a name="transfer-large-scale-db2-z-os-data-to-amazon-s3-in-csv-files-prereqs"></a>

**Prerequisites**
+ An IBM z/OS operating system user with authorization to run Restructured Extended Executor (REXX) and JCL scripts.
+ Access to z/OS Unix System Services (USS) to generate SSH (Secure Shell) private and public keys.
+ A writable S3 bucket. For more information, see [Create your first S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html) in the Amazon S3 documentation.
+ An AWS Transfer Family SSH File Transfer Protocol (SFTP)-enabled server using **Service managed** as the identity provider and Amazon S3 as the AWS storage service. For more information, see [Create an SFTP-enabled server](https://docs.aws.amazon.com/transfer/latest/userguide/create-server-sftp.html) in the AWS Transfer Family documentation.

**Limitations**
+ This approach isn’t suitable for near real-time or real-time data synchronization.
+ Data can be moved only from Db2 z/OS to Amazon S3, not the other way around.

## Architecture
<a name="transfer-large-scale-db2-z-os-data-to-amazon-s3-in-csv-files-architecture"></a>

**Source technology stack**
+ Mainframe running Db2 on z/OS

**Target technology stack**
+ AWS Transfer Family
+ Amazon S3
+ Amazon Athena
+ Amazon QuickSight
+ AWS Glue
+ Amazon Relational Database Service (Amazon RDS)
+ Amazon Aurora
+ Amazon Redshift

**Source and target architecture**

The following diagram shows the process for generating, extracting, and transferring Db2 z/OS data in ASCII CSV format to an S3 bucket.

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/66e6fa1a-1c7d-4b7a-8404-9ba85e433b24/images/87b13e0d-0be9-4462-bdbf-67342334416c.png)

1. A list of tables is selected for data migration from the Db2 catalog.

1. The list is used to drive the generation of unload jobs with the numeric and data columns in the external format.

1. The data is then transferred over to Amazon S3 by using AWS Transfer Family.

1. An AWS Glue extract, transform, and load (ETL) job can transform the data and load it to a processed bucket in the specified format, or AWS Glue can feed the data directly into the database.

1. Amazon Athena and Amazon QuickSight can be used to query and render the data to drive analytics.

The following diagram shows a logical flow of the entire process.

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/66e6fa1a-1c7d-4b7a-8404-9ba85e433b24/images/d72f2572-10c9-43f9-b6c9-7e57c9a69d52.png)

1. The first JCL, called TABNAME, will use the Db2 utility DSNTIAUL to extract and generate the list of tables that you plan to unload from Db2. To choose your tables, you must manually adapt the SQL input to select and add filter criteria to include one or more Db2 schemas.

1. The second JCL, called REXXEXEC, will use the a JCL skeleton and the REXX program that is provided to process the Table list created by the JCL TABNAME and generate one JCL per table name. Each JCL will contain one step for unloading the table and another step for sending the file to the S3 bucket by using the SFTP protocol.

1. The last step consists of running the JCL to unload the table and transferring the file to AWS. The entire process can be automated using a scheduler on premises or on AWS.

## Tools
<a name="transfer-large-scale-db2-z-os-data-to-amazon-s3-in-csv-files-tools"></a>

**AWS services**
+ [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/what-is.html) is an interactive query service that helps you analyze data directly in Amazon Simple Storage Service (Amazon S3) by using standard SQL.
+ [Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html) is a fully managed relational database engine that's built for the cloud and compatible with MySQL and PostgreSQL.
+ [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html) is a fully managed extract, transform, and load (ETL) service. It helps you reliably categorize, clean, enrich, and move data between data stores and data streams.
+ [Amazon QuickSight](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html) is a cloud-scale business intelligence (BI) service that helps you visualize, analyze, and report your data in a single dashboard.
+ [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/gsg/getting-started.html) is a managed petabyte-scale data warehouse service in the AWS Cloud.
+ [Amazon Relational Database Service (Amazon RDS)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html) helps you set up, operate, and scale a relational database in the AWS Cloud.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.
+ [AWS Transfer Family](https://docs.aws.amazon.com/transfer/latest/userguide/what-is-aws-transfer-family.html) is a secure transfer service that enables you to transfer files into and out of AWS storage services.

**Mainframe tools**
+ [SSH File Transfer Protocol (SFTP)](https://www.ssh.com/academy/ssh/sftp-ssh-file-transfer-protocol) is a secure file transfer protocol that allows remote login to and file transfer between servers. SSH provides security by encrypting all traffic.
+ [DSNTIAUL](https://www.ibm.com/docs/en/db2-for-zos/11?topic=dpasp-dsntiaul-sample-program) is a sample program provided by IBM for unloading data.
+ [DSNUTILB](https://www.ibm.com/docs/en/db2-for-zos/11?topic=sharing-recommendations-utilities-in-coexistence) is a utilities batch program provided by IBM for unloading data with different options from DSNTIAUL.
+ [z/OS OpenSSH](https://www.ibm.com/docs/en/zos/2.4.0?topic=zbed-zos-openssh) is a port of Open Source Software SSH running on the Unix System Service under the IBM operating system z/OS. SSH is a secure, encrypted connection program between two computers running on a TCP/IP network. It provides multiple utilities, including ssh-keygen.
+ [REXX (Restructured Extended Executor)](https://www.ibm.com/docs/en/zos/2.1.0?topic=guide-learning-rexx-language) script is used to automate JCL generation with the Db2 Unload and SFTP steps.

**Code**

The code for this pattern is available in the GitHub [unloaddb2](https://github.com/aws-samples/unloaddb2-samples) repository.

## Best practices
<a name="transfer-large-scale-db2-z-os-data-to-amazon-s3-in-csv-files-best-practices"></a>

For the first unload, the generated JCLs should unload the entire table data.

After the first full unload, perform incremental unloads for better performance and cost savings. pdate the SQL query in the template JCL deck to accommodate any changes to the unload process.

You can convert the schema manually or by using a script on Lambda with the Db2 SYSPUNCH as an input. For an industrial process, [AWS Schema Conversion Tool (SCT)](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Source.DB2zOS.html) is the preferred option.

Finally, use a mainframe-based scheduler or a scheduler on AWS with an agent on the mainframe to help manage and automate the entire process.

## Epics
<a name="transfer-large-scale-db2-z-os-data-to-amazon-s3-in-csv-files-epics"></a>

### Set up the S3 bucket
<a name="set-up-the-s3-bucket"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the S3 bucket. | For instructions, see [Create your first S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html). | General AWS |

### Set up the Transfer Family server
<a name="set-up-the-transfer-family-server"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an SFTP-enabled server. | To open and create an SFTP server on the [AWS Transfer Family console](https://console.aws.amazon.com/transfer/), do the following:1. On the Choose protocols, page, select the **SFTP (SSH File Transfer Protocol) – file transfer over Secure Shell** check box.<br />2. For the identity provider, choose **Service managed**.<br />3. For the endpoint, choose **Publicly accessible**.<br />4. For the domain, choose **Amazon S3**.<br />5. On the **Configure additional details** page, keep the default settings.<br />6. Create the server.  | General AWS |
| Create an IAM role for Transfer Family. | To create an AWS Identity and Access Management (IAM) role for Transfer Family to access Amazon S3, follow the instructions in [Create an IAM role and policy](https://docs.aws.amazon.com/transfer/latest/userguide/requirements-roles.html).  | AWS administrator |
| Add an Amazon S3 service-managed user. | To add the Amazon S3 service-managed user, follow the instructions in the [AWS documentation](https://docs.aws.amazon.com/transfer/latest/userguide/service-managed-users.html#add-s3-user), and use your mainframe user ID. | General AWS |

### Secure the communication protocol
<a name="secure-the-communication-protocol"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the SSH key. | Under your mainframe USS environment, run the following command.<pre>ssh-keygen -t rsa</pre>When prompted for a passphrase, keep it empty. | Mainframe developer |
| Give the right authorization levels to the SSH folder and key files. | By default, the public and private keys will be stored in the user directory `/u/home/username/.ssh`.<br />You must give the authorization 644 to the key files and 700 to the folder.<pre>chmod 644 .ssh/id_rsa<br />chmod 700 .ssh</pre> | Mainframe developer |
| Copy the public key content to your Amazon S3 service-managed user. | To copy the USS-generated public key content, open the [AWS Transfer Family console](https://console.aws.amazon.com/transfer/).1. In the navigation pane, choose **Servers**.<br />2. Choose the identifier in the **Server ID** column to see the **Server details**<br />3. Under **Users**, choose a user name to see the **User details**<br />4. Under **SSH public keys**, choose **Add SSH public key** to add the public key to a user. For the SSH public key, enter your public key.Your key is validated by the service before you can add your new user.<br />5. Choose **Add key**.  | Mainframe developer |

### Generate the JCLs
<a name="generate-the-jcls"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Generate the in-scope Db2 table list. | Provide input SQL to create a list of the tables that are scoped for data migration. This step requires you to specify selection criteria quering the Db2 catalog table SYSIBM.SYSTABLES using a SQL where clause. Filters can be customized to include a specific schema or table names that start with a particular prefix or based on a timestamp for incremental unload. Output is captured in a physical sequential (PS) dataset on the mainframe. This dataset will act as input for the next phase of JCL generation.<br />Before you use the JCL TABNAME (You can rename it if necessary), make the following changes:1. Substitute <Jobcard> with a job class and a user that is authorized to run Db2 utilities.<br />2. Substitute <HLQ1> or customize the output dataset names to meet your site standards.<br />3. Update the STEPLIB stack of PDSEs (partitioned data set extended) according to your site standards. The example in this pattern uses the IBM defaults.<br />4. Substitute the PLAN name and LIB with your installation-specific values.<br />5. Substitute <Schema> and <Prefix> with your selection criteria for the Db2 catalog.<br />6. Save the resultant JCL in a PDS (partitioned data set) library.<br />7. Submit the JCL.<br />**Db2 table list extraction job**<pre><Jobcard><br />//* <br />//* UNLOAD ALL THE TABLE NAMES FOR A PARTICULAR SCHEMA<br />//* <br />//STEP01  EXEC PGM=IEFBR14<br />//* <br />//DD1      DD  DISP=(MOD,DELETE,DELETE),<br />//         UNIT=SYSDA,<br />//         SPACE=(1000,(1,1)),<br />//         DSN=<HLQ1>.DSN81210.TABLIST<br />//* <br />//DD2      DD  DISP=(MOD,DELETE,DELETE),<br />//         UNIT=SYSDA,<br />//         SPACE=(1000,(1,1)),<br />//         DSN=<HLQ1>.DSN81210.SYSPUNCH <br />//* <br />//UNLOAD  EXEC PGM=IKJEFT01,DYNAMNBR=20 <br />//SYSTSPRT DD  SYSOUT=* <br />//STEPLIB  DD  DISP=SHR,DSN=DSNC10.DBCG.SDSNEXIT<br />//         DD  DISP=SHR,DSN=DSNC10.SDSNLOAD<br />//         DD  DISP=SHR,DSN=CEE.SCEERUN <br />//         DD  DISP=SHR,DSN=DSNC10.DBCG.RUNLIB.LOAD <br />//SYSTSIN  DD  *<br />  DSN SYSTEM(DBCG) <br />  RUN  PROGRAM(DSNTIAUL) PLAN(DSNTIB12) PARMS('SQL') - <br />       LIB('DSNC10.DBCG.RUNLIB.LOAD')<br />  END<br />//SYSPRINT DD SYSOUT=*<br />//* <br />//SYSUDUMP DD SYSOUT=*<br />//* <br />//SYSREC00 DD DISP=(NEW,CATLG,DELETE),<br />//            UNIT=SYSDA,SPACE=(32760,(1000,500)),<br />//            DSN=<HLQ1>.DSN81210.TABLIST <br />//* <br />//SYSPUNCH DD DISP=(NEW,CATLG,DELETE), <br />//            UNIT=SYSDA,SPACE=(32760,(1000,500)),<br />//            VOL=SER=SCR03,RECFM=FB,LRECL=120,BLKSIZE=12 <br />//            DSN=<HLQ1>.DSN81210.SYSPUNCH <br />//* <br />//SYSIN    DD * <br />   SELECT CHAR(CREATOR), CHAR(NAME)<br />     FROM SYSIBM.SYSTABLES <br />    WHERE OWNER = '<Schema>' <br />      AND NAME LIKE '<Prefix>%' <br />      AND TYPE = 'T'; <br />/* </pre> | Mainframe developer |
| Modify the JCL templates. | The JCL templates that are provided with this pattern contain a generic job card and library names. However, most mainframe sites will have their own naming standards for dataset names, library names, and job cards. For example, a specific job class might be required to run Db2 jobs. The Job Entry Subsytem implementations JES2 and JES3 can impose additional changes. Standard load libraries might have a different first qualifier than `SYS1`, which is IBM default. Therefore, customize the templates to account for your site-specific standards before you run them.<br />Make the following changes in the skeleton JCL UNLDSKEL:1. Modify the job card with a job class and user that is authorized to run Db2 utilities.<br />2. Customize output dataset names to meet your site standards.<br />3. Update the STEPLIB stack of PDSEs according to your site standards. The example in this pattern uses the IBM defaults.<br />4. Substitute `<DSN>` with your Db2 subsystem name and correlation ID.<br />5. Save the resultant JCL in a PDS library that is part of your ISPSLIB stack, which is the standard skeleton template library for ISPF.<br />**Unload and SFTP JCL skeleton**<pre>//&USRPFX.U JOB (DB2UNLOAD),'JOB',CLASS=A,MSGCLASS=A, <br />//         TIME=1440,NOTIFY=&USRPFX<br />//* DELETE DATASETS<br />//STEP01   EXEC PGM=IEFBR14<br />//DD01     DD DISP=(MOD,DELETE,DELETE),<br />//            UNIT=SYSDA,<br />//            SPACE=(TRK,(1,1)),<br />// DSN=&USRPFX..DB2.PUNCH.&JOBNAME<br />//DD02     DD DISP=(MOD,DELETE,DELETE),<br />//            UNIT=SYSDA,<br />//            SPACE=(TRK,(1,1)),<br />// DSN=&USRPFX..DB2.UNLOAD.&JOBNAME<br />//*<br />//* RUNNING DB2 EXTRACTION BATCH JOB FOR AWS DEMO<br />//*<br />//UNLD01   EXEC PGM=DSNUTILB,REGION=0M,<br />// PARM='<DSN>,UNLOAD'<br />//STEPLIB  DD  DISP=SHR,DSN=DSNC10.DBCG.SDSNEXIT<br />//         DD  DISP=SHR,DSN=DSNC10.SDSNLOAD<br />//SYSPRINT DD  SYSOUT=*<br />//UTPRINT  DD  SYSOUT=*<br />//SYSOUT   DD  SYSOUT=*<br />//SYSPUN01 DD  DISP=(NEW,CATLG,DELETE),<br />//             SPACE=(CYL,(1,1),RLSE),<br />// DSN=&USRPFX..DB2.PUNCH.&JOBNAME<br />//SYSREC01 DD  DISP=(NEW,CATLG,DELETE),<br />//             SPACE=(CYL,(10,50),RLSE),<br />// DSN=&USRPFX..DB2.UNLOAD.&JOBNAME<br />//SYSPRINT DD SYSOUT=*<br />//SYSIN    DD *<br />  UNLOAD<br />  DELIMITED COLDEL ','<br />  FROM TABLE &TABNAME<br />  UNLDDN SYSREC01<br />  PUNCHDDN SYSPUN01<br />  SHRLEVEL CHANGE ISOLATION UR;<br /> /*<br />//*<br />//* FTP TO AMAZON S3 BACKED FTP SERVER IF UNLOAD WAS SUCCESSFUL<br />//*<br />//SFTP EXEC PGM=BPXBATCH,COND=(4,LE),REGION=0M<br />//STDPARM DD *<br /> SH cp "//'&USRPFX..DB2.UNLOAD.&JOBNAME'"<br />   &TABNAME..csv;<br /> echo "ascii             " >> uplcmd;<br /> echo "PUT &TABNAME..csv " >>>> uplcmd;<br /> sftp -b uplcmd -i .ssh/id_rsa &FTPUSER.@&FTPSITE;<br /> rm &TABNAME..csv;<br /> //SYSPRINT DD SYSOUT=*<br /> //STDOUT DD SYSOUT=*<br /> //STDENV DD *<br /> //STDERR DD SYSOUT=*                                                </pre><br />  | Mainframe developer |
| Generate the Mass Unload JCL. | This step involves running a REXX script under an ISPF environment by using JCL. Provide the list of in-scope tables created on the first step as input for mass JCL generation against the `TABLIST DD` name. The JCL will generate one new JCL per table name in a user-specified partitioned dataset specified against the `ISPFILE DD` name. Allocate this library beforehand. Each new JCL will have two steps: one step to unload the Db2 table into a file, and one step to send the file to the S3 bucket.<br />Make the following changes in the JCL REXXEXEC (you can change the name):1. Substitute `Job card user ID` with a mainframe user ID that has unload authority on the tables. Substitute `SYSPROC`, `ISPPLIB`, `ISPSLIB`, `ISPMLIB`, and `ISPTLIB` `<HLQ1>` value or customize the `DSN` to meet your site standards. To find out your installation-specific values, you use the command `TSO ISRDDN`.<br />2. Substitute `<MFUSER>` with a user ID that has job-running privileges in your installation.<br />3. Substitute `<FTPUSER>` with a user ID that has the USS and FTP privilege in your installation.. It is assumed that this user ID and its SSH security keys are in place in the appropriate Unix Systems Services directory on the mainframe.<br />4. Substitute `<AWS TransferFamily IP>` with the AWS Transfer Family IP address or the domain name. This address will be used for the SFTP step.<br />5. Submit the JCL after applying the site standard accommodation and updating the REXX program as described below.<br />**Mass JCL generation job**<pre>//RUNREXX JOB (CREATEJCL),'RUNS ISPF TABLIST',CLASS=A,MSGCLASS=A,      <br />//         TIME=1440,NOTIFY=&SYSUID<br />//* Most of the values required can be updated to your site specific<br />//* values using the command 'TSO ISRDDN' in your ISPF session. <br />//* Update all the lines tagged with //update marker to desired<br />//* site specific values. <br />//ISPF EXEC PGM=IKJEFT01,REGION=2048K,DYNAMNBR=25<br />//SYSPROC   DD DISP=SHR,DSN=USER.Z23D.CLIST<br />//SYSEXEC   DD DISP=SHR,DSN=<HLQ1>.TEST.REXXLIB<br />//ISPPLIB   DD DISP=SHR,DSN=ISP.SISPPENU<br />//ISPSLIB   DD DISP=SHR,DSN=ISP.SISPSENU<br />//          DD DISP=SHR,DSN=<HLQ1>.TEST.ISPSLIB<br />//ISPMLIB   DD DSN=ISP.SISPMENU,DISP=SHR<br />//ISPTLIB   DD DDNAME=ISPTABL<br />//          DD DSN=ISP.SISPTENU,DISP=SHR<br />//ISPTABL   DD LIKE=ISP.SISPTENU,UNIT=VIO<br />//ISPPROF   DD LIKE=ISP.SISPTENU,UNIT=VIO<br />//ISPLOG    DD SYSOUT=*,RECFM=VA,LRECL=125<br />//SYSPRINT  DD SYSOUT=*<br />//SYSTSPRT  DD SYSOUT=*<br />//SYSUDUMP  DD SYSOUT=*<br />//SYSDBOUT  DD SYSOUT=*<br />//SYSTSPRT  DD SYSOUT=*<br />//SYSUDUMP  DD SYSOUT=*<br />//SYSDBOUT  DD SYSOUT=*<br />//SYSHELP   DD DSN=SYS1.HELP,DISP=SHR <br />//SYSOUT    DD SYSOUT=*<br />//* Input list of tablenames<br />//TABLIST   DD DISP=SHR,DSN=<HLQ1>.DSN81210.TABLIST<br />//* Output pds<br />//ISPFILE   DD DISP=SHR,DSN=<HLQ1>.TEST.JOBGEN<br />//SYSTSIN   DD *<br />ISPSTART CMD(ZSTEPS <MFUSER> <FTPUSER> <AWS TransferFamily IP>)<br />/*</pre><br />Before you use the REXX script, make the following changes:1. Save the REXX script in a PDS library defined under the `SYSEXEC` stack in the JCL REXXEXEC edited in the previous step with ZSTEPS as the member name. If you want to rename it, you should update the JCL to accommodate your needs.<br />2. This script uses the trace option to print additional information in case there are errors. You can instead add error handling code after the `EXECIO`, `ISPEXEC`, and `TSO` statements, and remove the trace line.<br />3. This script generates member names by using the `LODnnnnn` naming convention, which can support up to 100,000 members. If you have more than 100,000 tables, use a shorter prefix, and adjust the numbers in the `tempjob` statement.<br />**ZSTEPS REXX script**<pre>/*REXX - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - */<br />/* 10/27/2021 - added new parms to accommodate ftp */<br />Trace "o" <br />    parse arg usrpfx ftpuser ftpsite<br />    Say "Start"<br />    Say "Ftpuser: " ftpuser "Ftpsite:" ftpsite<br />    Say "Reading table name list"<br />    "EXECIO * DISKR TABLIST (STEM LINE. FINIS"<br />    DO I = 1 TO LINE.0<br />      Say I<br />      suffix = I<br />      Say LINE.i<br />      Parse var LINE.i schema table rest<br />      tabname = schema !! "." !! table<br />      Say tabname<br />      tempjob= "LOD" !! RIGHT("0000" !! i, 5) <br />      jobname=tempjob<br />      Say tempjob<br />      ADDRESS ISPEXEC "FTOPEN "<br />      ADDRESS ISPEXEC "FTINCL UNLDSKEL"<br />      /* member will be saved in ISPDSN library allocated in JCL */<br />      ADDRESS ISPEXEC "FTCLOSE NAME("tempjob")"<br />    END<br /><br />    ADDRESS TSO "FREE F(TABLIST) "<br />    ADDRESS TSO "FREE F(ISPFILE) "<br /><br />exit 0</pre> | Mainframe developer |

### Run the JCLs
<a name="run-the-jcls"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Perform the Db2 Unload step. | After the JCL generation, you will have as many JCLs as you have tables that need to be unloaded.<br />This story uses a JCL-generated example to explain the structure and the most important steps.<br />No action is required on your part. The following information is for reference only. If your intention is to submit the JCLs that you have generated in the previous step, skip to the *Submit the LODnnnnn JCLs* task.<br />When unloading Db2 data using a JCL with the IBM provided DSNUTILB Db2 utility, you must make sure that the unloaded data does not contain compressed numeric data. To accomplish this, use the DSNUTILB `DELIMITED` parameter.<br />The `DELIMITED` parameter supports unloading the data in CSV format by adding a character as the delimiter and double quotation marks for the text field, removing the padding in the VARCHAR column, and converting all the numeric fields into EXTERNAL FORMAT, including the DATE fields.<br />The following example shows what the unload step in the generated JCL looks like, using the comma character as a delimiter.<pre>                            <br /> UNLOAD<br /> DELIMITED COLDEL ',' <br /> FROM TABLE SCHEMA_NAME.TBNAME<br /> UNLDDN SYSREC01<br /> PUNCHDDN SYSPUN01<br /> SHRLEVEL CHANGE ISOLATION UR;</pre> | Mainframe developer, System engineer |
| Perform the SFTP step. | To use the SFTP protocol from a JCL, use the BPXBATCH utility. <br />The SFTP utility can’t access the MVS datasets directly. You can use the copy command (`cp`) to copy the sequential file `&USRPFX..DB2.UNLOAD.&JOBNAME` to the USS directory, where it becomes `&TABNAME..csv`.<br />Run the `sftp` command using the private key (`id_rsa`) and using the RACF user ID as the user name to connect to the AWS Transfer Family IP address.<pre>SH cp "//'&USRPFX..DB2.UNLOAD.&JOBNAME'"<br />   &TABNAME..csv;<br /> echo "ascii             " >> uplcmd;<br /> echo "PUT &TABNAME..csv " >>>> uplcmd;<br /> sftp -b uplcmd -i .ssh/id_rsa &FTPUSER.@&FTP_TF_SITE;<br /> rm &TABNAME..csv; </pre> | Mainframe developer, System engineer |
| Submit the LODnnnnn JCLs. | The prior JCL has generated all LODnnnnn JCL  tables that need to be unloaded, transformed into CSV, and transferred to the S3 bucket.<br />Run the `submit` command on all the JCLs that have been generated. | Mainframe developer, System engineer |

## Related resources
<a name="transfer-large-scale-db2-z-os-data-to-amazon-s3-in-csv-files-resources"></a>

For more information about the different tools and solutions used in this document, see the following:
+ [z/OS OpenSSH User’s Guide](https://www-01.ibm.com/servers/resourcelink/svc00100.nsf/pages/zOSV2R4sc276806/$file/foto100_v2r4.pdf)
+ [Db2 z/OS – Sample UNLOAD control statements](https://www.ibm.com/docs/en/db2-for-zos/11?topic=unload-sample-control-statements)
+ [Db2 z/OS – Unloading delimited files](https://www.ibm.com/docs/en/db2-for-zos/11?topic=unload-unloading-delimited-files)
+ [Transfer Family – Create an SFTP-enabled server](https://docs.aws.amazon.com/transfer/latest/userguide/create-server-sftp.html)
+ [Transfer Family – Working with service-managed users](https://docs.aws.amazon.com/transfer/latest/userguide/service-managed-users.html)

## Additional information
<a name="transfer-large-scale-db2-z-os-data-to-amazon-s3-in-csv-files-additional"></a>

After you have your Db2 data on Amazon S3, you have many ways to develop new insights. Because Amazon S3 integrates with AWS data analytics services, you can freely consume or expose this data on the distributed side. For example, you can do the following:
+ Build a [data lake on Amazon S3](https://aws.amazon.com/products/storage/data-lake-storage/), and extract valuable insights by using query-in-place, analytics, and machine learning tools without moving the data.
+ Initiate a [Lambda function](https://aws.amazon.com/lambda/) by setting up a post-upload processing workflow that is integrated with AWS Transfer Family.
+ Develop new microservices for accessing the data in Amazon S3 or in [fully managed database](https://aws.amazon.com/free/database/?trk=ps_a134p000007CdNEAA0&trkCampaign=acq_paid_search_brand&sc_channel=PS&sc_campaign=acquisition_FR&sc_publisher=Google&sc_category=Database&sc_country=FR&sc_geo=EMEA&sc_outcome=acq&sc_detail=amazon%20relational%20database%20service&sc_content=Relational%20Database_e&sc_matchtype=e&sc_segment=548727697660&sc_medium=ACQ-P|PS-GO|Brand|Desktop|SU|Database|Solution|FR|EN|Text&s_kwcid=AL!4422!3!548727697660!e!!g!!amazon%20relational%20database%20service&ef_id=CjwKCAjwzt6LBhBeEiwAbPGOgcGbQIl1-QsbHfWTgMZSSHEXzSG377R9ZyK3tCcbnHuT45L230FufxoCeEkQAvD_BwE:G:s&s_kwcid=AL!4422!3!548727697660!e!!g!!amazon%20relational%20database%20service) by using [AWS Glue](https://aws.amazon.com/glue/), which is a serverless data integration service that makes it easy to discover, prepare, and combine data for analytics, machine learning, and application development.

In a migration use case, because you can transfer any data from the mainframe to S3, you can do the following:
+ Retire physical infrastructure, and create a cost-effective data archival strategy with Amazon S3 Glacier and S3 Glacier Deep Archive.
+ Build scalable, durable, and secure backup and restore solutions with Amazon S3 and other AWS services, such as S3 Glacier and Amazon Elastic File System (Amazon EFS), to augment or replace existing on-premises capabilities.
