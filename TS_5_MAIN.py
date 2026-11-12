"""
Auteurs: Christian Clay et Kevin Tran
Description: Programme principal de gestion d'artistes musicaux.
Présente une interface graphique Tkinter qui permet à l'utilisateur
de créer, modifier, supprimer et afficher des artistes ainsi que leurs
listes de chansons.
"""

import tkinter as tk
from tkinter import messagebox
from TS_5_CLASS import Artiste

# Variables pour les codes de couleur, les polices et les tailles.

STR_COULEUR_FOND = "#f0f4f8"
STR_COULEUR_TEXTE = "#2c3e50"
STR_COULEUR_BTN_BLEU = "#2980b9"
STR_COULEUR_BTN_VERT = "#27ae60"
STR_COULEUR_BTN_ROUGE = "#e74c3c"
STR_COULEUR_BTN_GRIS = "#7f8c8d"
STR_POLICE_TITRE = ("Arial", 15, "bold")
STR_POLICE_SOUS_TITRE = ("Arial", 12, "bold")
STR_POLICE_NORMALE = ("Arial", 11)
STR_POLICE_MENU = ("Arial", 11, "bold")
INT_LARGEUR_BTN = 22

# Dictionnaire qui stocke les artistes avec leur nom comme clé et
# l'objet Artiste comme valeur.
dct_artistes = {}

# Fonctions utilitaires

def mettre_a_jour_liste_principale():
    # Efface la listbox et la remplit à nouveau pour avec les noms de
    # l'état actuel du dictionnaire.
    lbx_artistes.delete(0, tk.END)
    for str_nom in dct_artistes:
        lbx_artistes.insert(tk.END, str_nom)


def creer_fenetre_secondaire(str_titre, str_geometrie=None):
  
    # Crée et retourne une fenêtre secondaire avec paramètres standardisés.

    # Paramètres: str_titre: Titre de la fenêtre. str_geometrie: Géométrie optionnelle.

    fen = tk.Toplevel(fen_principale)
    fen.title(str_titre)
    fen.config(bg=STR_COULEUR_FOND)
    
     # Bloque l'interaction avec les autres fenêtres tant que celle-ci est ouverte.
    fen.grab_set()
    
    if str_geometrie:
        fen.geometry(str_geometrie)
    return fen


def creer_bouton(fen_parent, str_texte, str_couleur, cmd, int_largeur=12):

    # Crée et retourne un bouton avec paramètres standardisés.

    return tk.Button(fen_parent, text=str_texte, font=STR_POLICE_MENU, bg=str_couleur,
                     fg="white", width=int_largeur, relief="raised", command=cmd)


# Option 1: Créer un artiste.

def ouvrir_creer():

    # Liste temporaire pour stocker les chansons avant la création officielle de l'artiste.
    lst_chansons_temp = []

    fen_creer = creer_fenetre_secondaire("Créer un artiste")

    lbl_titre_creer = tk.Label(fen_creer, text="Créer un artiste",
        font=STR_POLICE_TITRE, bg=STR_COULEUR_FOND, fg=STR_COULEUR_TEXTE)
    lbl_titre_creer.grid(row=0, column=0, columnspan=4, pady=(15, 10))

    lbl_nom = tk.Label(fen_creer, text="Nom :", font=STR_POLICE_NORMALE,
        bg=STR_COULEUR_FOND, fg=STR_COULEUR_TEXTE)
    lbl_nom.grid(row=1, column=0, sticky="e", padx=(20, 5), pady=5)
    
    ent_nom = tk.Entry(fen_creer, font=STR_POLICE_NORMALE, width=22, justify="center")
    ent_nom.grid(row=1, column=1, padx=(5, 20), pady=5)

    lbl_genre = tk.Label(fen_creer, text="Genre musical :", font=STR_POLICE_NORMALE,
        bg=STR_COULEUR_FOND, fg=STR_COULEUR_TEXTE)
    lbl_genre.grid(row=2, column=0, sticky="e", padx=(20, 5), pady=5)
    
    ent_genre = tk.Entry(fen_creer, font=STR_POLICE_NORMALE, width=22, justify="center")
    ent_genre.grid(row=2, column=1, padx=(5, 20), pady=5)

    lbl_annee = tk.Label(fen_creer, text="Année de début :", font=STR_POLICE_NORMALE,
        bg=STR_COULEUR_FOND, fg=STR_COULEUR_TEXTE)
    lbl_annee.grid(row=3, column=0, sticky="e", padx=(20, 5), pady=5)
    
    ent_annee = tk.Entry(fen_creer, font=STR_POLICE_NORMALE, width=22, justify="center")
    ent_annee.grid(row=3, column=1, padx=(5, 20), pady=5)

    lbl_pays = tk.Label(fen_creer, text="Pays d'origine :", font=STR_POLICE_NORMALE,
        bg=STR_COULEUR_FOND, fg=STR_COULEUR_TEXTE)
    lbl_pays.grid(row=4, column=0, sticky="e", padx=(20, 5), pady=5)
    
    ent_pays = tk.Entry(fen_creer, font=STR_POLICE_NORMALE, width=22, justify="center")
    ent_pays.grid(row=4, column=1, padx=(5, 20), pady=5)

    lbl_titre_chansons = tk.Label(fen_creer, text="Ajouter des chansons",
        font=STR_POLICE_SOUS_TITRE, bg=STR_COULEUR_FOND, fg=STR_COULEUR_TEXTE)
    lbl_titre_chansons.grid(row=5, column=0, columnspan=2, pady=(15, 5))

    ent_chanson = tk.Entry(fen_creer, font=STR_POLICE_NORMALE, width=22, justify="center")
    ent_chanson.grid(row=6, column=0, columnspan=2, padx=20, pady=5)
   
    lbl_titre_liste_chansons = tk.Label(fen_creer, text="Chansons ajoutées:",
            font=STR_POLICE_SOUS_TITRE, bg=STR_COULEUR_FOND, fg=STR_COULEUR_TEXTE)
    lbl_titre_liste_chansons.grid(row=1, column=2, columnspan=2, pady=(10, 5), padx=30)

    lbx_chansons = tk.Listbox(fen_creer, height=12, width=28, font=STR_POLICE_NORMALE)
    lbx_chansons.grid(row=2, column=2, columnspan=2, rowspan=7, padx=30, pady=5)


    def ajouter_chanson():
        # Fonction qui permet l'utilisateur à ajouter des chansons à la liste de chansons de l'artiste.
    
        str_chanson = ent_chanson.get().strip()
        if str_chanson == "":
            messagebox.showerror("Erreur", "Le nom de la chanson ne peut pas être vide.", parent=fen_creer)
            return
        
        if str_chanson in lst_chansons_temp:
            messagebox.showerror("Erreur", "Cette chanson est déjà dans la liste.", parent=fen_creer)
            return
        
        lst_chansons_temp.append(str_chanson)
        lbx_chansons.insert(tk.END, str_chanson)
        ent_chanson.delete(0, tk.END)

    btn_ajouter_chanson = creer_bouton(fen_creer, "Ajouter la chanson", STR_COULEUR_BTN_BLEU, ajouter_chanson, 18)
    btn_ajouter_chanson.grid(row=7, column=0, columnspan=2, pady=15)

    def creer_artiste():
        # Fonction qui crée l'artiste (objet).
        
        str_nom = ent_nom.get().strip()
        str_genre = ent_genre.get().strip()
        str_annee = ent_annee.get().strip()
        str_pays = ent_pays.get().strip()
        
        # Vérifie que les boîtes d'entrée ne sont pas vides.
        if not str_nom or not str_genre or not str_annee or not str_pays:
            messagebox.showerror("Erreur", "Tous les champs doivent être remplis.", parent=fen_creer)
            return

        # Vérifie que le nom d'artiste ne se répète pas.
        if str_nom in dct_artistes:
            messagebox.showerror("Erreur", f"Un artiste nommé '{str_nom}' existe déjà.", parent=fen_creer)
            return

        # Vérifie que l'année est une donnée de type int.
        try:
            int_annee = int(str_annee)
        except ValueError:
            messagebox.showerror("Erreur", "L'année de début doit être un nombre entier.", parent=fen_creer)
            return
        
        try:
            # La création de l'objet déclenche le setter qui valide l'année.
            # Le setter de int_annee lève une ValueError si l'année est hors de 0-2026.
            nouvel_artiste = Artiste(str_nom, str_genre, int_annee, str_pays, lst_chansons_temp.copy())
        except ValueError as phrase_erreur:
            messagebox.showerror("Erreur", str(phrase_erreur), parent=fen_creer)
            return
         
        dct_artistes[str_nom] = nouvel_artiste
        
        mettre_a_jour_liste_principale()
        
        messagebox.showinfo("Succès", f"L'artiste '{str_nom}' a été créé avec succès !", parent=fen_creer)
        fen_creer.destroy()

    btn_creer_artiste = creer_bouton(fen_creer, "Créer l'artiste", STR_COULEUR_BTN_VERT, creer_artiste)
    btn_creer_artiste.grid(row=8, column=0, columnspan=2, pady=(10, 20))


# Option 2: Modifier un artiste.

def ouvrir_modifier_selectionne(fen_selection, str_nom_selectionne):

    artiste = dct_artistes[str_nom_selectionne]

    # Copie temporaire pour éviter de modifier la liste originale avant que
    # l'utilisateur confirme les changements.
    lst_chansons_temp = artiste.lst_chansons.copy()
    
    fen_modifier = creer_fenetre_secondaire("Modifier l'artiste sélectionné", "950x520")

    lbl_titre_modifier = tk.Label(fen_modifier, text=f"Modifier: {str_nom_selectionne}",
        font=STR_POLICE_TITRE, bg=STR_COULEUR_FOND, fg=STR_COULEUR_TEXTE)
    lbl_titre_modifier.grid(row=0, column=0, columnspan=5, pady=(15, 10))

    # Anciennes valeurs
    
    lbl_ancien_nom = tk.Label(fen_modifier, text=f"Ancien nom: {artiste.str_nom}",
        font=STR_POLICE_NORMALE, bg=STR_COULEUR_FOND, fg="#7f8c8d")
    lbl_ancien_nom.grid(row=1, column=0, sticky="w", padx=(20, 10), pady=4)

    lbl_ancien_genre = tk.Label(fen_modifier, text=f"Ancien genre: {artiste.str_genre}",
        font=STR_POLICE_NORMALE, bg=STR_COULEUR_FOND, fg="#7f8c8d")
    lbl_ancien_genre.grid(row=2, column=0, sticky="w", padx=(20, 10), pady=4)

    lbl_ancienne_annee = tk.Label(fen_modifier, text=f"Ancienne année: {artiste.int_annee}",
        font=STR_POLICE_NORMALE, bg=STR_COULEUR_FOND, fg="#7f8c8d")
    lbl_ancienne_annee.grid(row=3, column=0, sticky="w", padx=(20, 10), pady=4)

    lbl_ancien_pays = tk.Label(fen_modifier, text=f"Ancien pays: {artiste.str_pays}",
        font=STR_POLICE_NORMALE, bg=STR_COULEUR_FOND, fg="#7f8c8d")
    lbl_ancien_pays.grid(row=4, column=0, sticky="w", padx=(20, 10), pady=4)

    # Nouvelles valeurs
    
    lbl_nouveau_nom = tk.Label(fen_modifier, text="Nouveau nom:",
        font=STR_POLICE_SOUS_TITRE, bg=STR_COULEUR_FOND, fg=STR_COULEUR_TEXTE)
    lbl_nouveau_nom.grid(row=1, column=1, sticky="e", padx=5, pady=4)
    
    ent_nouveau_nom = tk.Entry(fen_modifier, font=STR_POLICE_NORMALE, width=22)
    ent_nouveau_nom.insert(0, artiste.str_nom)
    ent_nouveau_nom.grid(row=1, column=2, padx=(5, 20), pady=4)

    lbl_nouveau_genre = tk.Label(fen_modifier, text="Nouveau genre:",
        font=STR_POLICE_SOUS_TITRE, bg=STR_COULEUR_FOND, fg=STR_COULEUR_TEXTE)
    lbl_nouveau_genre.grid(row=2, column=1, sticky="e", padx=5, pady=4)
    
    ent_nouveau_genre = tk.Entry(fen_modifier, font=STR_POLICE_NORMALE, width=22)
    ent_nouveau_genre.insert(0, artiste.str_genre)
    ent_nouveau_genre.grid(row=2, column=2, padx=(5, 20), pady=4)

    lbl_nouvelle_annee = tk.Label(fen_modifier, text="Nouvelle année:",
        font=STR_POLICE_SOUS_TITRE, bg=STR_COULEUR_FOND, fg=STR_COULEUR_TEXTE)
    lbl_nouvelle_annee.grid(row=3, column=1, sticky="e", padx=5, pady=4)
    
    ent_nouvelle_annee = tk.Entry(fen_modifier, font=STR_POLICE_NORMALE, width=22)
    ent_nouvelle_annee.insert(0, str(artiste.int_annee))
    ent_nouvelle_annee.grid(row=3, column=2, padx=(5, 20), pady=4)

    lbl_nouveau_pays = tk.Label(fen_modifier, text="Nouveau pays:",
        font=STR_POLICE_SOUS_TITRE, bg=STR_COULEUR_FOND, fg=STR_COULEUR_TEXTE)
    lbl_nouveau_pays.grid(row=4, column=1, sticky="e", padx=5, pady=4)
    
    ent_nouveau_pays = tk.Entry(fen_modifier, font=STR_POLICE_NORMALE, width=22)
    ent_nouveau_pays.insert(0, artiste.str_pays)
    ent_nouveau_pays.grid(row=4, column=2, padx=(5, 20), pady=4)

    # Section modification des chansons
    
    lbl_titre_chansons = tk.Label(fen_modifier, text="Modifier les chansons:",
        font=STR_POLICE_SOUS_TITRE, bg=STR_COULEUR_FOND, fg=STR_COULEUR_TEXTE)
    lbl_titre_chansons.grid(row=5, column=0, columnspan=3, pady=(15, 5))

    lbx_chansons_modif = tk.Listbox(fen_modifier, height=8, width=32, font=STR_POLICE_NORMALE)
    lbx_chansons_modif.grid(row=6, column=0, columnspan=3, padx=20, pady=5, rowspan=3)

    def rafraichir_liste_chansons():
        # Remplit la listbox avec la liste de chansons.
        
        lbx_chansons_modif.delete(0, tk.END)
        for str_chanson in lst_chansons_temp:
            lbx_chansons_modif.insert(tk.END, str_chanson)

    rafraichir_liste_chansons()

    ent_nouvelle_chanson = tk.Entry(fen_modifier, font=STR_POLICE_NORMALE, width=32, justify="center")
    ent_nouvelle_chanson.grid(row=9, column=0, columnspan=3, padx=20, pady=(10, 5))

    def ajouter_nouvelle_chanson():
        
        str_chanson = ent_nouvelle_chanson.get().strip()
        if str_chanson == "":
            messagebox.showerror("Erreur", "Le nom de la chanson ne peut pas être vide.", parent=fen_modifier)
            return
        if str_chanson in lst_chansons_temp:
            messagebox.showerror("Erreur", "Cette chanson existe déjà dans la liste.", parent=fen_modifier)
            return
        
        lst_chansons_temp.append(str_chanson)
        rafraichir_liste_chansons()
        ent_nouvelle_chanson.delete(0, tk.END)

    def supprimer_chanson_selectionnee():
        # Fonction qui permet à l'utilisateur de supprimer les chansons souhaitées de la liste. 
        
        selection = lbx_chansons_modif.curselection()
        
        if not selection:
            messagebox.showerror("Erreur", "Veuillez sélectionner une chanson à supprimer.", parent=fen_modifier)
            return
        
        int_index = selection[0]
        lst_chansons_temp.pop(int_index)
        rafraichir_liste_chansons()

    btn_ajouter_chanson_modif = creer_bouton(fen_modifier, "Ajouter", STR_COULEUR_BTN_BLEU, ajouter_nouvelle_chanson, 14)
    btn_ajouter_chanson_modif.grid(row=10, column=0, pady=5)

    btn_supprimer_chanson_modif = creer_bouton(fen_modifier, "Supprimer sélection", STR_COULEUR_BTN_ROUGE, supprimer_chanson_selectionnee, 18)
    btn_supprimer_chanson_modif.grid(row=10, column=1, columnspan=2, pady=5)

    def valider_modifications():
        
        str_nouveau_nom = ent_nouveau_nom.get().strip()
        str_nouveau_genre = ent_nouveau_genre.get().strip()
        str_nouvelle_annee = ent_nouvelle_annee.get().strip()
        str_nouveau_pays = ent_nouveau_pays.get().strip()

        if not str_nouveau_nom or not str_nouveau_genre or not str_nouvelle_annee or not str_nouveau_pays:
            messagebox.showerror("Erreur", "Tous les champs doivent être remplis.", parent=fen_modifier)
            return

        if str_nouveau_nom != str_nom_selectionne and str_nouveau_nom in dct_artistes:
            messagebox.showerror("Erreur", f"Un artiste nommé '{str_nouveau_nom}' existe déjà.", parent=fen_modifier)
            return

        try:
            int_nouvelle_annee = int(str_nouvelle_annee) 
        except ValueError:
            messagebox.showerror("Erreur", "L'année de début doit être un nombre entier.", parent=fen_modifier)
            return
        
        try:
            artiste.int_annee = int_nouvelle_annee
        except ValueError as phrase_erreur:
            messagebox.showerror("Erreur", str(phrase_erreur), parent=fen_modifier)
            return

        artiste.str_nom = str_nouveau_nom
        artiste.str_genre = str_nouveau_genre
        artiste.str_pays = str_nouveau_pays
        artiste.lst_chansons = lst_chansons_temp.copy()

        if str_nouveau_nom != str_nom_selectionne:
            # Remplace l'ancienne clé par la nouvelle dans le dictionnaire sans perdre les données.
            dct_artistes[str_nouveau_nom] = dct_artistes.pop(str_nom_selectionne)

        mettre_a_jour_liste_principale()
        messagebox.showinfo("Succès", f"Le profil de l'artiste '{str_nouveau_nom}' a été modifié avec succès !", parent=fen_modifier)
        fen_modifier.destroy()
        fen_selection.destroy()

    btn_enregistrer = creer_bouton(fen_modifier, "Enregistrer les modifications", STR_COULEUR_BTN_VERT, valider_modifications, 26)
    btn_enregistrer.grid(row=11, column=0, columnspan=3, pady=(20, 15))


def ouvrir_modifier():
   
    if not dct_artistes:
        messagebox.showerror("Aucun artiste", "Aucun artiste dans le système. Veuillez d'abord en créer un.")
        return

    fen_selection_modifier = creer_fenetre_secondaire("Modifier un artiste")

    lbl_titre_sel = tk.Label(fen_selection_modifier, text="Sélectionnez un artiste à modifier :",
        font=STR_POLICE_SOUS_TITRE, bg=STR_COULEUR_FOND, fg=STR_COULEUR_TEXTE)
    lbl_titre_sel.grid(row=0, column=0, columnspan=2, pady=(15, 5), padx=35)

    lbx_selection_modifier = tk.Listbox(fen_selection_modifier, width=30, height=12, font=STR_POLICE_NORMALE)
    lbx_selection_modifier.grid(row=1, column=0, columnspan=2, padx=35, pady=5)

    for str_nom in dct_artistes.keys():
        lbx_selection_modifier.insert(tk.END, str_nom)

    def gerer_selection_modifier():
      
        selection = lbx_selection_modifier.curselection()
        
        if not selection:
            messagebox.showerror("Erreur", "Veuillez sélectionner un artiste dans la liste.", parent=fen_selection_modifier)
            return
        
        str_nom_selectionne = lbx_selection_modifier.get(selection[0])
        ouvrir_modifier_selectionne(fen_selection_modifier, str_nom_selectionne)

    btn_modifier_selectionne = creer_bouton(fen_selection_modifier, "Modifier l'artiste sélectionné", STR_COULEUR_BTN_BLEU, gerer_selection_modifier, 26)
    btn_modifier_selectionne.grid(row=2, column=0, columnspan=2, pady=(10, 20))


# Option 3: Supprimer un artiste.

def ouvrir_supprimer():
  
    if not dct_artistes:
        messagebox.showerror("Aucun artiste", "Aucun artiste dans le système. Veuillez d'abord en créer un.")
        return

    fen_supprimer = creer_fenetre_secondaire("Supprimer un artiste")

    lbl_titre_supp = tk.Label(fen_supprimer, text="Sélectionnez un artiste à supprimer :",
        font=STR_POLICE_SOUS_TITRE, bg=STR_COULEUR_FOND, fg=STR_COULEUR_TEXTE)
    lbl_titre_supp.grid(row=0, column=0, columnspan=2, pady=(15, 5), padx=20)

    lbx_choix_supp = tk.Listbox(fen_supprimer, width=30, height=12,
        font=STR_POLICE_NORMALE, bg="white", fg=STR_COULEUR_TEXTE, relief="raised")
    lbx_choix_supp.grid(row=1, column=0, columnspan=2, padx=20, pady=5)

    for str_nom in dct_artistes.keys():
        lbx_choix_supp.insert(tk.END, str_nom)

    def confirmer_suppression():

        selection = lbx_choix_supp.curselection()
        if not selection:
            messagebox.showerror("Erreur", "Veuillez sélectionner un artiste.", parent=fen_supprimer)
            return

        str_nom = lbx_choix_supp.get(selection[0])
        bool_confirme = messagebox.askyesno("Confirmer la suppression",
            f"Voulez-vous vraiment supprimer l'artiste '{str_nom}' ?",
            parent=fen_supprimer)

        if bool_confirme:
            
            del dct_artistes[str_nom]
            mettre_a_jour_liste_principale()
            messagebox.showinfo("Succès", f"L'artiste '{str_nom}' a été supprimé avec succès.", parent=fen_supprimer)
            fen_supprimer.destroy()

    btn_confirmer_supp = creer_bouton(fen_supprimer, "Supprimer", STR_COULEUR_BTN_ROUGE, confirmer_suppression)
    btn_confirmer_supp.grid(row=2, column=0, pady=(10, 20), padx=20)

    btn_annuler_supp = creer_bouton(fen_supprimer, "Annuler", STR_COULEUR_BTN_GRIS, fen_supprimer.destroy)
    btn_annuler_supp.grid(row=2, column=1, pady=(10, 20), padx=20)


# Option 4: Afficher un artiste.

def ouvrir_afficher():

    if not dct_artistes:
        messagebox.showerror("Aucun artiste", "Aucun artiste dans le système. Veuillez d'abord en créer un.")
        return

    fen_afficher = creer_fenetre_secondaire("Afficher les informations d'un artiste")

    lbl_titre_aff = tk.Label(fen_afficher, text="Sélectionnez un artiste à afficher :",
        font=STR_POLICE_SOUS_TITRE, bg=STR_COULEUR_FOND, fg=STR_COULEUR_TEXTE)
    lbl_titre_aff.grid(row=0, column=0, columnspan=2, pady=(15, 5), padx=20)

    lbx_choix_aff = tk.Listbox(fen_afficher, width=30, height=12,
        font=STR_POLICE_NORMALE, bg="white", fg=STR_COULEUR_TEXTE, relief="raised")
    lbx_choix_aff.grid(row=1, column=0, columnspan=2, padx=20, pady=5)

    for str_nom in dct_artistes.keys():
        lbx_choix_aff.insert(tk.END, str_nom)

    def ouvrir_details_artiste():
        
        selection = lbx_choix_aff.curselection()
        if not selection:
            messagebox.showerror("Erreur", "Veuillez sélectionner un artiste.", parent=fen_afficher)
            return

        str_nom = lbx_choix_aff.get(selection[0])
        artiste = dct_artistes[str_nom]

        fen_info = creer_fenetre_secondaire(f"Informations de {str_nom}")

        lbl_titre_info = tk.Label(fen_info, text=f"Fiche de l'artiste: {artiste.str_nom}",
            font=STR_POLICE_TITRE, bg=STR_COULEUR_FOND, fg=STR_COULEUR_TEXTE)
        lbl_titre_info.grid(row=0, column=0, columnspan=2, pady=(15, 10), padx=20)

        
        lbl_nom_titre = tk.Label(fen_info, text="Nom:",
        font=STR_POLICE_SOUS_TITRE, bg=STR_COULEUR_FOND, fg=STR_COULEUR_TEXTE)
        lbl_nom_titre.grid(row=1, column=0, sticky="e", padx=(20, 5), pady=4)

        lbl_nom_valeur = tk.Label(fen_info, text=artiste.str_nom,
        font=STR_POLICE_NORMALE, bg=STR_COULEUR_FOND, fg=STR_COULEUR_TEXTE)
        lbl_nom_valeur.grid(row=1, column=1, sticky="w", padx=(5, 20), pady=4)

        lbl_genre_titre = tk.Label(fen_info, text="Genre musical:",
        font=STR_POLICE_SOUS_TITRE, bg=STR_COULEUR_FOND, fg=STR_COULEUR_TEXTE)
        lbl_genre_titre.grid(row=2, column=0, sticky="e", padx=(20, 5), pady=4)

        lbl_genre_valeur = tk.Label(fen_info, text=artiste.str_genre,
        font=STR_POLICE_NORMALE, bg=STR_COULEUR_FOND, fg=STR_COULEUR_TEXTE)
        lbl_genre_valeur.grid(row=2, column=1, sticky="w", padx=(5, 20), pady=4)

        lbl_annee_titre = tk.Label(fen_info, text="Année de début:",
        font=STR_POLICE_SOUS_TITRE, bg=STR_COULEUR_FOND, fg=STR_COULEUR_TEXTE)
        lbl_annee_titre.grid(row=3, column=0, sticky="e", padx=(20, 5), pady=4)

        lbl_annee_valeur = tk.Label(fen_info, text=str(artiste.int_annee),
        font=STR_POLICE_NORMALE, bg=STR_COULEUR_FOND, fg=STR_COULEUR_TEXTE)
        lbl_annee_valeur.grid(row=3, column=1, sticky="w", padx=(5, 20), pady=4)

        lbl_pays_titre = tk.Label(fen_info, text="Pays d'origine:",
        font=STR_POLICE_SOUS_TITRE, bg=STR_COULEUR_FOND, fg=STR_COULEUR_TEXTE)
        lbl_pays_titre.grid(row=4, column=0, sticky="e", padx=(20, 5), pady=4)

        lbl_pays_valeur = tk.Label(fen_info, text=artiste.str_pays,
        font=STR_POLICE_NORMALE, bg=STR_COULEUR_FOND, fg=STR_COULEUR_TEXTE)
        lbl_pays_valeur.grid(row=4, column=1, sticky="w", padx=(5, 20), pady=4)

        lbl_titre_chansons_info = tk.Label(fen_info, text="Liste de chansons:",
            font=STR_POLICE_SOUS_TITRE, bg=STR_COULEUR_FOND, fg=STR_COULEUR_TEXTE)
        lbl_titre_chansons_info.grid(row=5, column=0, columnspan=2, sticky="w", padx=20, pady=(10, 5))

        if artiste.lst_chansons:
            
              # enumerate() retourne l'index (int_i) et la valeur (str_chanson) de chaque élément
              # de la liste en même temps.
            for int_i, str_chanson in enumerate(artiste.lst_chansons):
                
                lbl_chanson = tk.Label(fen_info, text=f"{int_i + 1}. {str_chanson}",
                font=STR_POLICE_NORMALE, bg=STR_COULEUR_FOND, fg=STR_COULEUR_TEXTE)
                lbl_chanson.grid(row=6 + int_i, column=0, columnspan=2, sticky="w", padx=30, pady=2)
                
            int_derniere_ligne = 6 + len(artiste.lst_chansons)

        else:
            
            lbl_aucune_chanson = tk.Label(fen_info, text="Aucune chanson enregistrée.",
            font=STR_POLICE_NORMALE, bg=STR_COULEUR_FOND, fg="#7f8c8d")
            lbl_aucune_chanson.grid(row=6, column=0, columnspan=2, sticky="w", padx=30)
            
            int_derniere_ligne = 7

        btn_fermer_info = creer_bouton(fen_info, "Fermer", STR_COULEUR_BTN_GRIS, fen_info.destroy)
        btn_fermer_info.grid(row=int_derniere_ligne + 1, column=0, columnspan=2, pady=(15, 20))

    btn_voir_details = creer_bouton(fen_afficher, "Voir les détails", STR_COULEUR_BTN_BLEU, ouvrir_details_artiste)
    btn_voir_details.grid(row=2, column=0, pady=(10, 20), padx=20)

    btn_annuler_aff = creer_bouton(fen_afficher, "Annuler", STR_COULEUR_BTN_GRIS, fen_afficher.destroy)
    btn_annuler_aff.grid(row=2, column=1, pady=(10, 20), padx=20)


# Option 5: Quitter le programme.

def quitter_programme():
    
    bool_confirme = messagebox.askyesno("Quitter", "Voulez-vous vraiment quitter le programme ?")
    if bool_confirme:
        fen_principale.destroy()

def bloquer_fermeture_x():
    messagebox.showwarning("Action impossible",
    "Veuillez utiliser le bouton '5 - Quitter' pour fermer le programme.")


# Fenêtre principale.

fen_principale = tk.Tk()
fen_principale.title("Gestionnaire d'artistes musicaux")
fen_principale.config(bg=STR_COULEUR_FOND)

# Empêche le redimensionnement de la fenêtre.
fen_principale.resizable(False, False)

lbl_titre_principal = tk.Label(fen_principale, text="Gestionnaire d'artistes musicaux",
    font=("Arial", 18, "bold"), bg=STR_COULEUR_FOND, fg=STR_COULEUR_TEXTE)
lbl_titre_principal.grid(row=0, column=0, columnspan=4, pady=(60, 5), padx=30)

img_notes = tk.PhotoImage(file="music_note.png")
lbl_img_notes = tk.Label(fen_principale, image=img_notes, bg=STR_COULEUR_FOND)
lbl_img_notes.grid(row=0, column=3, rowspan=2, padx=(0, 20), pady=(40, 0))

frm_menu = tk.Frame(fen_principale, bg=STR_COULEUR_FOND)
frm_menu.grid(row=3, column=0, columnspan=2, pady=20, padx=(30, 10))

lbl_menu = tk.Label(frm_menu, text="MENU",
    font=("Arial", 12, "bold"), bg=STR_COULEUR_FOND, fg=STR_COULEUR_TEXTE)
lbl_menu.grid(row=0, column=0, pady=(0, 10))

btn_creer = tk.Button(frm_menu, text="1 - Créer un artiste", font=STR_POLICE_NORMALE,
    bg=STR_COULEUR_BTN_BLEU, fg="white", width=INT_LARGEUR_BTN, pady=6, relief="raised", command=ouvrir_creer)
btn_creer.grid(row=1, column=0, padx=10, pady=4)

btn_modifier = tk.Button(frm_menu, text="2 - Modifier un artiste", font=STR_POLICE_NORMALE,
    bg=STR_COULEUR_BTN_BLEU, fg="white", width=INT_LARGEUR_BTN, pady=6, relief="raised", command=ouvrir_modifier)
btn_modifier.grid(row=2, column=0, padx=10, pady=4)

btn_supprimer = tk.Button(frm_menu, text="3 - Supprimer un artiste", font=STR_POLICE_NORMALE,
    bg=STR_COULEUR_BTN_BLEU, fg="white", width=INT_LARGEUR_BTN, pady=6, relief="raised", command=ouvrir_supprimer)
btn_supprimer.grid(row=3, column=0, padx=10, pady=4)

btn_afficher = tk.Button(frm_menu, text="4 - Afficher un artiste", font=STR_POLICE_NORMALE,
    bg=STR_COULEUR_BTN_BLEU, fg="white", width=INT_LARGEUR_BTN, pady=6, relief="raised", command=ouvrir_afficher)
btn_afficher.grid(row=4, column=0, padx=10, pady=4)

btn_quitter = tk.Button(frm_menu, text="5 - Quitter", font=STR_POLICE_NORMALE,
    bg=STR_COULEUR_BTN_ROUGE, fg="white", width=INT_LARGEUR_BTN, pady=6, relief="raised", command=quitter_programme)
btn_quitter.grid(row=5, column=0, padx=10, pady=4)


frm_liste = tk.Frame(fen_principale, bg=STR_COULEUR_FOND)
frm_liste.grid(row=3, column=2, padx=(10, 30), pady=20)

lbl_enregistres = tk.Label(frm_liste, text="ARTISTES ENREGISTRÉS",
    font=("Arial", 11, "bold"), bg=STR_COULEUR_FOND, fg=STR_COULEUR_TEXTE)
lbl_enregistres.grid(row=0, column=0, pady=(0, 10))

lbx_artistes = tk.Listbox(frm_liste, width=28, height=12,
    font=STR_POLICE_NORMALE, bg="white", fg=STR_COULEUR_TEXTE)
lbx_artistes.grid(row=1, column=0)

lbl_aide = tk.Label(frm_liste, text="Utilisez les boutons du menu pour gérer les artistes.",
    font=("Arial", 9, "italic"), bg=STR_COULEUR_FOND, fg="#95a5a6")
lbl_aide.grid(row=2, column=0, pady=(5, 0))

# Blocage du bouton X
fen_principale.protocol("WM_DELETE_WINDOW", bloquer_fermeture_x)

fen_principale.mainloop()
