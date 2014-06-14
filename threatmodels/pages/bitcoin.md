title: Bitcoin
Application: Bitcoin
date: 2014-06-06
Trusted Parties: Minority of clients in the network
Untrusted Parties: Majority of clients in the network
Key Storage: Local
Convenience: Medium
Authentication: Chain of cryptographic signatures
Architecture: P2P
tags:[Crypto-currency peer-to-peer]

# Intro
Bitcoin was the first and is the most widely used crypto-currency. It uses
novel cryptographic constructions to prevent double spending and to fully 
de-centralize the network. It has resisted attack for several years in the wild
and is generally considered very robust and secure.

# Trusted Parties
The trust comes from the fact that you believe that most of the computing power
on the network is controlled by clients who are behaving honestly. This is a
reasonable assumption because of the popularity of the crypto-currency and the
amount of attention that is paid to its status at any given moment. This is a
virtue of the direct monetary value of the system. The incentive to protect
the network is directly computable and that makes is more likely that honest
parties will expend resources to monitor it and protect it.

# Untrusted Parties
Because of the distributed nature of the Bitcoin network, and its requirement
for proof-of-work, an attacker needs to control a significant portion of the
computing power on the network in order for him/her to affect the networks
normal operation. This means that any single node, or any sufficiently small
group of nodes should be considered "untrusted".

# Key Storage
Clients in the Bitcoin network are responsible for protecting their secret
keys. This is the minimum level of required trust attainable in an encryption
system. Unfortunately, you must still trust your local machine in order to
trust that your keys are safe. Services do exist to store Bitcoin wallets
remotely, but those services are out of the scope of this threat model.

# Convenience
Bitcoin provides a unique service and in contrast to other services in the
payment sector (ignoring copycats) it solves a whole host of problems, while
providing unparalleled security and anonymity as well as robustness. The
secret keys must still be properly managed by the user and therefore,
Bitcoin only receives a score of medium on the convenience scale.

# Authentication
The authentication in the Bitcoin network takes place in the block chain and is
an ingenious way of protecting the public record of transactions. In order for
a new block to get added to the chain, clients must solve a "hard" computation
that includes a signature of the previous blocks. Changing a block requires
exponential effort and changing an older block requires re-computing all the
subsequent blocks. This proof-of-work model means that cheating is made more
expensive that it''s worth. This is true security.

# Architecture
There is no central authority in the Bitcoin network, and it could even operate
without a constant internet connection if it needed to. This is known as a
peer-to-peer architecture. Peer-to-peer architectures like the Bitcoin network
provide security that other architectures can not. Because there is no central
server, shutting down the network completely would mean cutting off each and
every node in the network. This means that a denial-of-service attack is
especially difficult to execute against the Bitcoin network.

