### Factures de Vente

Les factures de vente disposent d'un format d'impression spécifique appelé "Facture Suisse" (Swiss Invoice).

Ce format dispose des particularités suivantes:


1. Il propose deux champs additionnels nommés "Référence" et "Sujet".
Ceux-ci sont accessibles dans la section "Informations de Référence" de la facture de vente.

S'ils ne sont pas remplis, ils n'apparaissent pas sur la facture.


2. Il imprime l'adresse du client suivant le format défini dans le "Modèle d'Adresse" du pays.
Pour la Suisse, le format de base est le suivant:

```
{{ address_line1 }}<br>{% if address_line2 %}{{ address_line2 }}<br>{% endif -%}
{% if pincode %}{{ pincode }} {% endif -%}{{ city }}<br>
{{ country }}
```
Ce format est installé automatiquement lors de l'installation de l'application.
Vous pouvez bien évidemment le modifier dans les modèles d'adresse d'ERPNext.


3. Vous avez la possibilité d'imprimer les rabais par article en cochant l'option "Imprimer les Rabais par Article" dans la section "Réglages d'Impression".
Dans ce cas une colonne additionnelle "Rabais" apparaîtra dans votre tableau d'articles.


4. Pour diviser votre tableau en plusieurs sections (chaque section sera imprimée sur une page différente), sélectionnez "Saut de Page" depuis une ligne d'article.


5. Si vous avez fait une remise supplémentaire, celle-ci apparaîtra accompagné du total net entre le sous-total du tableau et les lignes de Taxes et Frais.


6. Le libellé de TVA est celui de la désignation de la ligne de TVA/Frais.
Pour la TVA, il est configurable dans le module "Comptes" > "Modèle de Taxes et Frais de Vente"


7. Tous les nombres sont arrondis à 2 décimales, indépendamment des réglages généraux d'ERPNext.


8. Le Total Général ou "Total" est arrondi à 2 décimales, à 5 centimes près.
