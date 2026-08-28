---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-legacy-applications-from-oracle-pro-c-to-ecpg.html
---

# Migrate legacy applications from Oracle Pro\*C to ECPG
<a name="migrate-legacy-applications-from-oracle-pro-c-to-ecpg"></a>

*Sai Parthasaradhi and Mahesh Balumuri, Amazon Web Services*

## Summary
<a name="migrate-legacy-applications-from-oracle-pro-c-to-ecpg-summary"></a>

Most legacy applications that have embedded SQL code use the Oracle Pro\*C precompiler to access the database. When you migrate these Oracle databases to Amazon Relational Database Service (Amazon RDS) for PostgreSQL or Amazon Aurora PostgreSQL-Compatible Edition, you have to convert your application code to a format that’s compatible with the precompiler in PostgreSQL, which is called ECPG. This pattern describes how to convert Oracle Pro\*C code to its equivalent in PostgreSQL ECPG.

For more information about Pro\*C, see the [Oracle documentation](https://docs.oracle.com/cd/E11882_01/appdev.112/e10825/pc_01int.htm#i2415). For a brief introduction to ECPG, see the [Additional information](#migrate-legacy-applications-from-oracle-pro-c-to-ecpg-additional) section.

## Prerequisites and limitations
<a name="migrate-legacy-applications-from-oracle-pro-c-to-ecpg-prereqs"></a>

**Prerequisites **
+ An active AWS account
+ An Amazon RDS for PostgreSQL or Aurora PostgreSQL-Compatible database
+ An Oracle database running on premises

## Tools
<a name="migrate-legacy-applications-from-oracle-pro-c-to-ecpg-tools"></a>
+ The PostgreSQL packages listed in the next section.
+ [AWS CLI ](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html)– The AWS Command Line Interface (AWS CLI) is an open-source tool for interacting with AWS services through commands in your command-line shell. With minimal configuration, you can run AWS CLI commands that implement functionality equivalent to that provided by the browser-based AWS Management Console from a command prompt.

## Epics
<a name="migrate-legacy-applications-from-oracle-pro-c-to-ecpg-epics"></a>

### Set the build environment on CentOS or RHEL
<a name="set-the-build-environment-on-centos-or-rhel"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Install PostgreSQL packages. | Install the required PostgreSQL packages by using the following commands.<pre>yum update -y<br />yum install -y yum-utils<br />rpm -ivh https://download.postgresql.org/pub/repos/yum/reporpms/EL-8-x86_64/pgdg-redhat-repo-latest.noarch.rpm<br />dnf -qy module disable postgresql</pre> | App developer, DevOps engineer |
| Install the header files and libraries. | Install the `postgresql12-devel` package, which contains header files and libraries, by using the following commands. Install the package in both the development and the runtime environments to avoid errors in the runtime environment.<pre>dnf -y install postgresql12-devel<br />yum install ncompress zip ghostscript jq unzip wget git -y</pre><br />For the development environment only, also run the following commands.<pre>yum install zlib-devel make -y<br />ln -s /usr/pgsql-12/bin/ecpg /usr/bin/</pre> | App developer, DevOps engineer |
| Configure the environment path variable. | Set the environment path for PostgreSQL client libraries.<pre>export PATH=$PATH:/usr/pgsql-12/bin</pre> | App developer, DevOps engineer |
| Install additional software as necessary. | If required, install **pgLoader** as a replacement for **SQL\*Loader** in Oracle.<pre>wget -O /etc/yum.repos.d/pgloader-ccl.repo https://dl.packager.io/srv/opf/pgloader-ccl/master/installer/el/7.repo<br />yum install pgloader-ccl -y<br />ln -s /opt/pgloader-ccl/bin/pgloader /usr/bin/</pre><br />If you’re calling any Java applications from Pro\*C modules, install Java.<pre>yum install java -y</pre><br />Install **ant** to compile the Java code.<pre>yum install ant -y</pre> | App developer, DevOps engineer |
| Install the AWS CLI. | Install the AWS CLI to run commands to interact with AWS services such as AWS Secrets Manager and Amazon Simple Storage Service (Amazon S3) from your applications.<pre>cd /tmp/<br />curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"<br />unzip awscliv2.zip<br />./aws/install -i /usr/local/aws-cli -b /usr/local/bin --update</pre> | App developer, DevOps engineer |
| Identify the programs to be converted. | Identify the applications that you want to convert from Pro\*C to ECPG. | App developer, App owner |

### Convert Pro\*C code to ECPG
<a name="convert-pro-c-code-to-ecpg"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Remove unwanted headers. | Remove the `include `headers that are not required in PostgreSQL, such as `oci.h`, `oratypes`, and `sqlda`. | App owner, App developer |
| Update variable declarations. | Add `EXEC SQL` statements for all variable declarations that are used as host variables.<br />Remove the `EXEC SQL VAR` declarations such as the following from your application.<pre>EXEC SQL VAR query IS STRING(2048);</pre> | App developer, App owner |
| Update ROWNUM functionality. | The `ROWNUM` function isn’t available in PostgreSQL. Replace this with the `ROW_NUMBER` window function in SQL queries.<br />Pro\*C code:<pre>SELECT SUBSTR(RTRIM(FILE_NAME,'.txt'),12) INTO :gcpclFileseq  <br />FROM   (SELECT FILE_NAME <br />FROM  DEMO_FILES_TABLE <br />WHERE FILE_NAME    LIKE '%POC%' <br />ORDER BY FILE_NAME DESC) FL2 <br />WHERE ROWNUM <=1 ORDER BY ROWNUM;</pre><br />ECPG code:<pre>SELECT SUBSTR(RTRIM(FILE_NAME,'.txt'),12) INTO :gcpclFileseq  <br />FROM   (SELECT FILE_NAME , ROW_NUMBER() OVER (ORDER BY FILE_NAME DESC) AS ROWNUM<br />FROM  demo_schema.DEMO_FILES_TABLE <br />WHERE FILE_NAME    LIKE '%POC%'<br />ORDER BY FILE_NAME DESC) FL2 <br />WHERE ROWNUM <=1 ORDER BY ROWNUM; </pre> | App developer, App owner |
| Update function parameters to use alias variables. | In PostgreSQL, function parameters can’t be used as host variables. Overwrite them by using an alias variable.<br />Pro\*C code:<pre>int processData(int referenceId){<br />  EXEC SQL char col_val[100];<br />  EXEC SQL select column_name INTO :col_val from table_name where col=:referenceId;<br />}</pre><br />ECPG code:<pre>int processData(int referenceIdParam){<br />  EXEC SQL int referenceId = referenceIdParam;<br />  EXEC SQL char col_val[100];<br />  EXEC SQL select column_name INTO :col_val from table_name where col=:referenceId;<br />}</pre> | App developer, App owner |
| Update struct types. | Define `struct` types in `EXEC SQL BEGIN` and `END` blocks with `typedef` if the `struct` type variables are used as host variables. If the `struct` types are defined in header (`.h`) files, include the files with `EXEC SQL` include statements.<br />Pro\*C code:<br />Header file (`demo.h`)<pre>struct s_partition_ranges<br />{<br /> char   sc_table_group[31];<br /> char   sc_table_name[31];<br /> char   sc_range_value[10];<br />}; <br />struct s_partition_ranges_ind<br />{<br />  short    ss_table_group;<br />  short    ss_table_name;<br />  short    ss_range_value;<br />}; </pre><br />ECPG code:<br />Header file (`demo.h`)<pre>EXEC SQL BEGIN DECLARE SECTION;<br />typedef struct <br />{<br />  char   sc_table_group[31];<br />  char   sc_table_name[31];<br />  char   sc_range_value[10];<br />} s_partition_ranges; <br />typedef struct <br />{<br />  short    ss_table_group;<br />  short    ss_table_name;<br />  short    ss_range_value;<br />} s_partition_ranges_ind; <br />EXEC SQL END DECLARE SECTION;</pre><br />Pro\*C file (`demo.pc`)<pre>#include "demo.h"<br />struct s_partition_ranges gc_partition_data[MAX_PART_TABLE] ;<br />struct s_partition_ranges_ind gc_partition_data_ind[MAX_PART_TABLE] ;</pre><br />ECPG file (`demo.pc`)<pre>exec sql include "demo.h"<br />EXEC SQL BEGIN DECLARE SECTION;<br />s_partition_ranges gc_partition_data[MAX_PART_TABLE] ;<br />s_partition_ranges_ind gc_partition_data_ind[MAX_PART_TABLE] ;<br />EXEC SQL END DECLARE SECTION;</pre> | App developer, App owner |
| Modify logic to fetch from cursors. | To fetch multiple rows from cursors by using array variables, change the code to use `FETCH FORWARD`.<br />Pro\*C code:<pre>EXEC SQL char  aPoeFiles[MAX_FILES][FILENAME_LENGTH];<br />EXEC SQL FETCH filename_cursor into :aPoeFiles;</pre><br />ECPG code:<pre>EXEC SQL char  aPoeFiles[MAX_FILES][FILENAME_LENGTH];<br />EXEC SQL int fetchSize = MAX_FILES;<br />EXEC SQL FETCH FORWARD :fetchSize filename_cursor into :aPoeFiles;</pre> | App developer, App owner |
| Modify package calls that don't have return values. | Oracle package functions that don’t have return values should be called with an indicator variable. If your application includes multiple functions that have the same name or if the unknown type functions generate runtime errors, typecast the values to the data types.<br />Pro\*C code:<pre>void ProcessData (char *data , int id)<br />{        <br />        EXEC SQL EXECUTE<br />               BEGIN<br />                  pkg_demo.process_data (:data, :id);                                                                                    <br />               END;<br />       END-EXEC;<br />}</pre><br />ECPG code:<pre>void ProcessData (char *dataParam, int idParam )<br />{<br />        EXEC SQL char *data = dataParam;<br />        EXEC SQL int id = idParam;<br />        EXEC SQL short rowInd;<br />        EXEC SQL short rowInd = 0;<br />        EXEC SQL SELECT pkg_demo.process_data (<br />                       inp_data => :data::text,<br />                       inp_id => :id<br />               ) INTO :rowInd;<br />}</pre> | App developer, App owner |
| Rewrite SQL\_CURSOR variables. | Rewrite the `SQL_CURSOR` variable and its implementation.<br />Pro\*C code:<pre>/* SQL Cursor */<br />SQL_CURSOR      demo_cursor;<br />EXEC SQL ALLOCATE :demo_cursor;<br />EXEC SQL EXECUTE<br />  BEGIN<br />      pkg_demo.get_cursor(     <br />        demo_cur=>:demo_cursor<br />      );<br />  END;<br />END-EXEC;</pre><br />ECPG code:<pre>EXEC SQL DECLARE demo_cursor CURSOR FOR SELECT<br />         * from<br />    pkg_demo.open_filename_rc(<br />            demo_cur=>refcursor<br />          ) ;<br />EXEC SQL char open_filename_rcInd[100]; <br /># As the below function returns cursor_name as <br /># return we need to use char[] type as indicator. <br />EXEC SQL SELECT pkg_demo.get_cursor (<br />        demo_cur=>'demo_cursor'<br />    ) INTO :open_filename_rcInd;</pre> | App developer, App owner |
| Apply common migration patterns. | + Change SQL queries so they’re compatible with PostgreSQL.<br />+ Move anonymous blocks, when they aren’t supported in ECPG, to the database.<br />+ Remove `dbms_application_info` logic, which isn’t supported by PostgreSQL.<br />+ Move `EXEC SQL COMMIT` statements after the cursor close. If you commit queries while in the loop to fetch the records from the cursor, the cursor is closed and a cursor doesn’t exist error is displayed.<br />+ For information about handling exceptions in ECPG and error codes, see [Error Handling](https://www.postgresql.org/docs/12/ecpg-errors.html) in the PostgreSQL documentation. | App developer, App owner |
| Enable debugging, if required.  | To run the ECPG program in debug mode, add the following command inside the main function block.<pre>ECPGdebug(1, stderr); </pre> | App developer, App owner |

### Compile ECPG programs
<a name="compile-ecpg-programs"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an executable file for ECPG. | If you have an embedded SQL C source file named `prog1.pgc`, you can create an executable program by using the following sequence of commands.<pre>ecpg prog1.pgc<br />cc -I/usr/local/pgsql/include -c prog1.c<br />cc -o prog1 prog1.o -L/usr/local/pgsql/lib -lecpg</pre> | App developer, App owner |
| Create a make file for compilation. | Create a make file to compile the ECPG program, as shown in the following sample file.<pre>CFLAGS ::= $(CFLAGS) -I/usr/pgsql-12/include -g -Wall<br />LDFLAGS ::= $(LDFLAGS) -L/usr/pgsql-12/lib -Wl,-rpath,/usr/pgsql-12/lib<br />LDLIBS ::= $(LDLIBS) -lecpg<br />PROGRAMS = test <br />.PHONY: all clean<br />%.c: %.pgc<br />      ecpg $<<br />all: $(PROGRAMS)<br />clean:<br />    rm -f $(PROGRAMS) $(PROGRAMS:%=%.c) $(PROGRAMS:%=%.o)</pre> | App developer, App owner |

### Test the application
<a name="test-the-application"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Test the code. | Test the converted application code to make sure that it functions correctly. | App developer, App owner, Test engineer |

## Related resources
<a name="migrate-legacy-applications-from-oracle-pro-c-to-ecpg-resources"></a>
+ [ECPG - Embedded SQL in C](https://www.postgresql.org/docs/current/static/ecpg.html) (PostgreSQL documentation)
+ [Error Handling](https://www.postgresql.org/docs/12/ecpg-errors.html) (PostgreSQL documentation)
+ [Why Use the Oracle Pro\*C/C\+\+ Precompiler](https://docs.oracle.com/cd/E11882_01/appdev.112/e10825/pc_01int.htm#i2415) (Oracle documentation)

## Additional information
<a name="migrate-legacy-applications-from-oracle-pro-c-to-ecpg-additional"></a>

PostgreSQL has an embedded SQL precompiler, ECPG, which is equivalent to the Oracle Pro\*C precompiler. ECPG converts C programs that have embedded SQL statements to standard C code by replacing the SQL calls with special function calls. The output files can then be processed with any C compiler tool chain.

**Input and output files**

ECPG converts each input file you specify on the command line to the corresponding C output file. If an input file name doesn’t have a file extension, .pgc is assumed. The file's extension is replaced by `.c` to construct the output file name. However, you can override the default output file name by using the `-o` option.

If you use a dash (`-`) as the input file name, ECPG reads the program from standard input and writes to standard output, unless you override that by using the `-o` option.

**Header files**

When the PostgreSQL compiler compiles the pre-processed C code files, it looks for the ECPG header files in the PostgreSQL `include` directory. Therefore, you might have to use the `-I` option to point the compiler to the correct directory (for example, `-I/usr/local/pgsql/include`).

**Libraries**

Programs that use C code with embedded SQL have to be linked against the `libecpg` library. For example, you can use the linker options` -L/usr/local/pgsql/lib -lecpg`.

Converted ECPG applications call functions in the `libpq` library through the embedded SQL library (`ecpglib`), and communicate with the PostgreSQL server by using the standard frontend/backend protocol.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
