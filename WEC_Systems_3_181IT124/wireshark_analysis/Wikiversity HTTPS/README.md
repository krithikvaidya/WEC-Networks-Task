Analysing **HTTPS** traffic in Wireshark is a bit more complicated, as
the packets are encrypted. In this example, we will capture the traffic
when we visit [Wikiversity](https://en.wikiversity.org/), that uses HTTPS.
We will apply the *ssl* display filter to view the packets sent over HTTPS.

To find the specific packets that are relevant only to the website we are
visiting, we search for the packet with the *Info* field set to **Client Hello**
This indicates the beggining of the Handshake procedure between our system, (the
client) and the server. The destination IP address corresponding to this packet 
is the IP address we are looking for.

// TODO

*Reference* - https://en.m.wikiversity.org/wiki/Wireshark/HTTPS