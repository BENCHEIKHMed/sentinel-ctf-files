# === Sentinel CTF — Docker Escape Challenge ===
# 
# Ce conteneur est intentionnellement mal configuré.
# Objectif : évasion du conteneur pour lire /flag.txt sur l'hôte.
#
# Pour lancer localement :
#   docker build -t docker-escape .
#   docker run --privileged -it docker-escape /bin/bash
#   FLAG = FLAG{d0ck3r_3sc4p3_pr1v1l3g3d}
#
# (Créez /flag.txt sur l'hôte avant de lancer le conteneur)

FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
    bash curl wget netcat-openbsd \
    util-linux mount procps \
    && rm -rf /var/lib/apt/lists/*

# Le flag est sur le système HÔTE, pas dans le conteneur
RUN echo "Ce fichier n'est pas le flag. Le flag est sur l'hôte." > /flag.txt

WORKDIR /challenge
COPY challenge_info.txt .

CMD ["/bin/bash"]
