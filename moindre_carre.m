% Donn�es exp�rimentales
d = [3, 6.6, 9.5, 15, 22.5, 28.8]; % Distances en m�tres
A_p = [62.7, 70, 72.75, 82.75, 90, 93]; % Att�nuation mesur�e en dB

% Constante K (calcul�e � partir de vos notes)
K = -40; % Exemple, d�j� donn� dans l'image

% Mod�le th�orique pour A_th�o
model = @(gamma, d) -K + 10 * gamma * log10(d);

% Fonction d'erreur quadratique � minimiser
error_func = @(gamma) sum((model(gamma, d) - A_p).^2);

% Estimation initiale pour gamma
gamma_initial = 2;

% Minimisation avec fminsearch
gamma_opt = fminsearch(error_func, gamma_initial);

% Affichage du r�sultat
disp(['Valeur optimis�e de gamma : ', num2str(gamma_opt)]);

% Trac� des r�sultats
A_theo = model(gamma_opt, d);
figure;
plot(log10(d), A_p, 'o', 'DisplayName', 'Donn�es exp�rimentales');
hold on;
plot(log10(d), A_theo, '-r', 'DisplayName', 'Mod�le ajust�');
xlabel('Log_{10}(Distance)');
ylabel('Att�nuation (dB)');
legend('Location', 'Best');
title('Ajustement par moindres carr�s');
grid on;
