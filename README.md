# DNS-Server

Implemented a simplified DNS system consisting of a Client program and two server programs: 
  RS (a simplified root DNS server) and TS (a simplified top-level DNS server)
  
The Client program has two sockets: one used to communicate with the RS server and the other is for the TS server
  
The RS and TS programs each maintain a DNS_table consisting of three fields:
 - Hostname
 - IP address
 - Flag (A or NS)

**Program Outline: **
1. Client connects to the RS sever, sending the queried hostname as a string.
2. The RS program does a look up in its DNS_table, and if there is a match, sends the entry as a string
     Hostname IPaddress A
3. If there is no match, RS sends the string
     TSHostname - NS
  where TShostname is the name of the machine on which the TS program is running.
4. The client then sends the queried hostname as a string to TS. 
5. The TS program looks up the hostname in its DNS_table, and if there is a match, sends the entry as a string:
     Hostname IP address A
  Otherwise, it sends an error string
     Hostname - Error:HOST NOT FOUND
