### Factures de Vente

Les factures de vente disposent d'un format d'impression spécifique appelé "Facture Suisse" (Swiss Invoice).

Ce format dispose des particularités suivantes:


- Il propose deux champs additionnels nommés "Référence" et "Sujet".
Ceux-ci sont accessibles dans la section "Informations de Référence" de la facture de vente.
S'ils ne sont pas remplis, ils n'apparaissent pas sur la facture.


- Il imprime l'adresse du client suivant le format défini dans le "Modèle d'Adresse" du pays.


Ce format est installé automatiquement lors de l'installation de l'application.
Vous pouvez bien évidemment le modifier dans les modèles d'adresse d'ERPNext.


- Vous avez la possibilité d'imprimer les rabais par article en cochant l'option "Imprimer les Rabais par Article" dans la section "Réglages d'Impression".
Dans ce cas une colonne additionnelle "Rabais" apparaîtra dans votre tableau d'articles.


- Pour diviser votre tableau en plusieurs sections (chaque section sera imprimée sur une page différente), sélectionnez "Saut de Page" depuis une ligne d'article.


- Si vous avez fait une remise supplémentaire, celle-ci apparaîtra accompagné du total net entre le sous-total du tableau et les lignes de Taxes et Frais.


- Le libellé de TVA est celui de la désignation de la ligne de TVA-Frais.
Pour la TVA, il est configurable dans le module "Comptes" > "Modèle de Taxes et Frais de Vente"


- Tous les nombres sont arrondis à 2 décimales, indépendamment des réglages généraux d'ERPNext.


- Le Total Général ou "Total" est arrondi à 2 décimales, à 5 centimes près.
