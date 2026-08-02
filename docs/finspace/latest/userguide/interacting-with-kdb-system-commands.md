---
source_url: https://docs.aws.amazon.com/finspace/latest/userguide/interacting-with-kdb-system-commands.html
---

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html).

# Supported system commands
<a name="interacting-with-kdb-system-commands"></a>

 System commands control the q environment. The following table shows a list of system commands that FinSpace supports.

<table>
<thead>
  <tr><th>System commands</th><th>Description</th><th>Constraints</th></tr>
</thead>
<tbody>
  <tr><td>\\a</td><td>Lists all the tables in the current namespace.</td><td>None</td></tr>
  <tr><td>\\awk</td><td>A pattern scanning and text processing language.</td><td>Only available on General purpose and HDB clusters.</td></tr>
  <tr><td>\\b</td><td>Lists all the views (derived tables).</td><td rowspan="2">None</td></tr>
  <tr><td>\\B</td><td>Lists all the pending views.</td></tr>
  <tr><td>\\base64</td><td>Encodes or decodes data in base64 format.</td><td>Only available on General purpose and HDB clusters.</td></tr>
  <tr><td>\\c</td><td>Shows or sets the console size.</td><td rowspan="2">None</td></tr>
  <tr><td>\\C</td><td>Shows or sets the HTTP response size.</td></tr>
  <tr><td>\\cat</td><td>Concatenates and display files.</td><td rowspan="4">Only available on General purpose and HDB clusters.</td></tr>
  <tr><td>\\cd</td><td>Shows or sets the current directory.</td></tr>
  <tr><td>\\cp</td><td>Copies files or directories.</td></tr>
  <tr><td>\\curl</td><td>Transfers data to or from a web server using HTTP, HTTPS, SCP, SFTP, TFTP, and more.</td></tr>
  <tr><td>\\d</td><td>Changes the current namespace.</td><td>None</td></tr>
  <tr><td>\\dirname</td><td>Removes the last component of a file name, leaving the directory path.</td><td>Only available on General purpose and HDB clusters.</td></tr>
  <tr><td>\\e</td><td>Governs error trapping for client requests.</td><td>None</td></tr>
  <tr><td>\\echo</td><td>Displays text or variables to the standard output.</td><td rowspan="2">Only available on General purpose and HDB clusters.</td></tr>
  <tr><td>\\egrep</td><td>Searches for a pattern in one or more input files (extended grep).</td></tr>
  <tr><td>\\f</td><td>Lists all functions in the current namespace.</td><td>None</td></tr>
  <tr><td>\\find</td><td>Searches for files based on various criteria such as name, size, and modification time.</td><td>Only available on General purpose and HDB clusters.</td></tr>
  <tr><td>\\g</td><td>Shows or sets garbage-collection mode.</td><td>None</td></tr>
  <tr><td>\\grep</td><td>Looks for a pattern in one or more input files.</td><td rowspan="4">Only available on General purpose and HDB clusters.</td></tr>
  <tr><td>\\gunzip</td><td>Uncompresses a file or list of files.</td></tr>
  <tr><td>\\gzip</td><td>Compresses a file or list of files.</td></tr>
  <tr><td>\\jq</td><td>A lightweight and flexible command-line JSON processor.</td></tr>
  <tr><td>\\l</td><td>Loads a script or data from a file or directory.</td><td>None</td></tr>
  <tr><td>\\ln</td><td>Creates a hard link or symbolic link to a file.</td><td rowspan="5">Only available on General purpose and HDB clusters.</td></tr>
  <tr><td>\\ls</td><td>Lists information about files and directories.</td></tr>
  <tr><td>\\mkdir</td><td>Creates a new directory.</td></tr>
  <tr><td>\\mv</td><td>Moves or renames files or directories.</td></tr>
  <tr><td>\\nohup</td><td>Runs a command immune to hangups, allowing it to continue running in the background.</td></tr>
  <tr><td>\\o</td><td>Shows or sets the offset from Coordinated Universal Time (UTC).</td><td>None</td></tr>
  <tr><td>\\p</td><td>Shows or sets the TCP port on which the q session listens.</td><td>FinSpace supports this command with no arguments, which gets the current port. It is only permitted with argument 443 (noop), not permitted with other arguments. </td></tr>
  <tr><td>\\P</td><td>Sets the display precision for floating-point numbers.</td><td>None</td></tr>
  <tr><td>\\pgrep</td><td>Looks up or signal processes based on name and other attributes.</td><td rowspan="3">Only available on General purpose and HDB clusters.</td></tr>
  <tr><td>\\ps</td><td>Displays information about running processes.</td></tr>
  <tr><td>\\pwd</td><td>Prints the current working directory.</td></tr>
  <tr><td>\\r</td><td>Renames a file.</td><td>None</td></tr>
  <tr><td>\\readlink</td><td>Displays the value of a symbolic link.</td><td rowspan="3">Only available on General purpose and HDB clusters.</td></tr>
  <tr><td>\\rm</td><td>Removes files or directories.</td></tr>
  <tr><td>\\rmdir</td><td>Removes empty directories.</td></tr>
  <tr><td>\\s</td><td>Shows or sets the number of secondary threads available.</td><td rowspan="2">None</td></tr>
  <tr><td>\\S</td><td>Shows or sets the value of the random seed.</td></tr>
  <tr><td>\\sed</td><td>A stream editor that filters and transforms text.</td><td rowspan="2">Only available on General purpose and HDB clusters.</td></tr>
  <tr><td>\\sleep</td><td>Suspends execution for a specified period of time.</td></tr>
  <tr><td>\\t</td><td>Shows or sets the timer interrupt in milliseconds.</td><td>FinSpace supports this command but it is not fully functional as the function called by the timer can only be set by the init script. </td></tr>
  <tr><td>\\T</td><td>Shows or sets the client execution timeout.</td><td>None</td></tr>
  <tr><td>\\touch</td><td>Creates a new file or updates the timestamp of an existing file.</td><td rowspan="2">Only available on General purpose and HDB clusters.</td></tr>
  <tr><td>\\tr</td><td>Translates or deletes characters from standard input.</td></tr>
  <tr><td>\\ts</td><td>Runs an expression and shows the runtime and memory used.</td><td>None</td></tr>
  <tr><td>\\unzip</td><td>Extracts files from a ZIP archive.</td><td>Only available on General purpose and HDB clusters.</td></tr>
  <tr><td>\\v</td><td>Lists variables in the current or specified namespace.</td><td rowspan="3">None</td></tr>
  <tr><td>\\w</td><td>Shows memory usage or sets workspace memory limit.</td></tr>
  <tr><td>\\W</td><td>Shows or sets the start-of-week offset.</td></tr>
  <tr><td>\\wc</td><td>Counts the number of lines, words, and characters in one or more files.</td><td rowspan="2">Only available on General purpose and HDB clusters.</td></tr>
  <tr><td>\\xargs</td><td>Builds and executes command lines from standard input.</td></tr>
  <tr><td>\\z</td><td>Shows or sets the format for date parsing.</td><td>None</td></tr>
  <tr><td>\\zip</td><td>Packages and compresses files into a ZIP archive.</td><td>Only available on General purpose and HDB clusters.</td></tr>
  <tr><td>\\\_</td><td>In debugger’s prompt, clears one level from the execution stack or toggles between the q and k interpreters.</td><td rowspan="3">None</td></tr>
  <tr><td>\\1</td><td>Redirects stdout to files from within the q session.</td></tr>
  <tr><td>\\2</td><td>Redirects stderr to files from within the q session.</td></tr>
</tbody>
</table>

## Helper environment variables
<a name="interacting-with-kdb-writeable-dir"></a>

You can quickly access user directories through the following environment variables that return a string of the folder path.

| Helper environment variables  | Use for  | Directory |
| --- | --- | --- |
| .aws.akcp | Primary user code path. | /opt/kx/app/code |
| .aws.akcsp | Secondary user code path that's available only for **General purpose** cluster. | /opt/kx/app/code\_scratch |
| .aws.akscp | Primarily used for handling savedown functionality with an RDB cluster. | /opt/kx/app/scratch |

## Loading databases relative to code directory
<a name="loading-db-code-dir"></a>

We have added a symlink to the code directory to allow loading of database relative to the code path. For example, if the database is labeled as *kxDatabase* and the current working directory is /`opt/kx/app/code` then the database can be loaded as `\l /kxDatabase`.
