% Données expérimentales
d = [3, 6.6, 9.5, 15, 22.5, 28.8]; % Distances en mètres
A_p = [62.7, 70, 72.75, 82.75, 90, 93]; % Atténuation mesurée en dB

% Constante K (calculée à partir de vos notes)
K = -40; % Exemple, déjà donné dans l'image

% Modèle théorique pour A_théo
model = @(gamma, d) -K + 10 * gamma * log10(d);

% Fonction d'erreur quadratique à minimiser
error_func = @(gamma) sum((model(gamma, d) - A_p).^2);

% Estimation initiale pour gamma
gamma_initial = 2;

% Minimisation avec fminsearch
gamma_opt = fminsearch(error_func, gamma_initial);

% Affichage du résultat
disp(['Valeur optimisée de gamma : ', num2str(gamma_opt)]);

% Tracé des résultats
A_theo = model(gamma_opt, d);
figure;
plot(log10(d), A_p, 'o', 'DisplayName', 'Données expérimentales');
hold on;
plot(log10(d), A_theo, '-r', 'DisplayName', 'Modèle ajusté');
xlabel('Log_{10}(Distance)');
ylabel('Atténuation (dB)');
legend('Location', 'Best');
title('Ajustement par moindres carrés');
grid on;
