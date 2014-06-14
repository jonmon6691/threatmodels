title: TOR
Application: TOR
date: 2014-6-13
Trusted Parties: Local Machine, TOR Exit node
Untrusted Parties: Remote servers, TOR relay nodes
Key Storage: Local
Convenience: High
Authentication: Anonymous
Architecture: Peer-to-peer with super-nodes
tags:[ Anonymity-network ]

# Intro
Tor was originally known as the acronym TOR which stands for The Onion Router,
but has since become a name in and of itself. The Tor network is a service
designed to provide anonymity to internet users by encrypting their traffic
and bouncing it between several other nodes. These nodes are actually just
other Tor users' computers. The last node releases the traffic to the internet
through a special node called a Tor exit node and is the only node that can see
the unencrypted traffic. However, the encryption scheme that Tor uses makes it
so that none of the nodes along the way know where the traffic came from or
where it is going, including the special exit node.

# Trusted Parties
As usual, you must always trust your local machine. A key logger or just about
any malware completely compromises your privacy and your security on the
internet.  The trusted party specific to the Tor network is the Tor exit node.
This node is capable of performing a man-in-the-middle attack on your traffic
because it is finally stripped of its encryption at this stage. It you aren't
using SSL, then this node can view and modify all of your traffic.

# Untrusted Parties
Another obvious entry here is that even though your identity is protected by
the network, the servers you visit can not be considered trusted and may
compromise your identity depending on what information you give them. Within
the TOR network, you are able to rely on the anonymity of the network even if
there are malicious nodes. Because your traffic is encrypted in layers, any
internal node does not know the source or destination or the content of the
traffic.

# Key Storage
You node's private key is held locally. 

# Convenience
Information about the network is held in a few central servers called super
nodes. This speeds up the key exchange procedure and increases the convenience
of using the network.

A browser is available that is designed with Tor built in as a proxy and is
specially designed to protect your identity at the application level. This
makes it very easy for regular users to hide their identity while using the
internet in mostly the same way that they normally would.

# Authentication
The point of the Tor network is to provide anonymity. There is no integral
authentication of the user. Authentication between nodes is provided by the
public-key encryption scheme when the route is first set up.

# Architecture
The Tor network is fundamentally a peer-to-peer network. Some information is
kept in central nodes to aid in the negotiation of circuits. This is a minor
security concern because a denial of service attack only needs to target these
nodes to be successful.
