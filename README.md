
# 🚀 Kubernetes Deployment Strategies: Blue/Green & Canary

Este repositorio demuestra la implementación de dos estrategias modernas de despliegue en Kubernetes: **Blue/Green** y **Canary**, utilizando un clúster local con Minikube. Se incluye además un sistema de prueba de carga con `k6`.

---

## 📦 Estructura del Proyecto

```
.
├── blue-green/        # Manifiestos para estrategia Blue/Green
├── canary/            # Manifiestos para estrategia Canary
├── web-server/        # Web server Flask con dos versiones (v1, v2)
├── load-test/         # Scripts de prueba de carga con k6
└── README.md          # Este archivo
```

---

## 🧰 Requisitos Previos

- [Docker](https://www.docker.com/products/docker-desktop/)
- [Minikube](https://minikube.sigs.k8s.io/docs/start/)
- [kubectl](https://kubernetes.io/docs/tasks/tools/)
- [k6](https://k6.io/docs/getting-started/installation/) (para pruebas de carga)

---

## ⚙️ 1. Levantar el clúster con Minikube

```bash
start docker app
minikube start --driver=docker
```

---

## 🐳 2. Construcción de Imágenes Docker

```bash
# Versión 1
cd web-server/v1
docker build -t web-v1:latest .

# Versión 2
cd ../v2
docker build -t web-v2:latest .
```

---

## 🧼 3. Cargar las imágenes en Minikube

```bash
minikube image load web-v1:latest
minikube image load web-v2:latest
```

---

## 💙💚 4. Despliegue Blue/Green

### Desplegar la versión inicial (v1)

```bash
kubectl apply -f blue-green/deployment-v1.yaml
kubectl apply -f blue-green/service.yaml
```

### Probar la versión activa

```bash
minikube service web-service
```

### Cambiar de Blue a Green (v2)

```bash
kubectl apply -f blue-green/deployment-v2.yaml

kubectl patch service web-service -p '{"spec":{"selector":{"app":"web","version":"v2"}}}'
```

---

## 🌗 5. Despliegue Canary

```bash
kubectl apply -f canary/deployment-stable.yaml
kubectl apply -f canary/deployment-canary.yaml
kubectl apply -f canary/service.yaml
kubectl apply -f canary/ingress.yaml
```

> Esto expone las versiones v1 y v2 simultáneamente. v2 con menos réplicas.

---

## 🔍 6. Ver Pods y Servicios

```bash
kubectl get pods
kubectl get svc
kubectl logs -l app=web --tail=10
```

---

## 📈 7. Pruebas de Carga con k6

### Instalar k6 (si aún no lo tenés)

```bash
brew install k6        # macOS
sudo apt install k6    # Ubuntu/Debian
```

### Ejecutar el test

Obtené la URL del servicio:

```bash
minikube service web-service --url
```

Reemplazá la URL en el archivo `load-test/test.js` y luego ejecutá:

```bash
cd load-test
k6 run test.js
```

---

## 🧽 8. Limpieza del entorno

```bash
kubectl delete all --all
```

---

## 🛡️ Buenas Prácticas Incluidas

- Contenedores que no corren como root (`USER nobody`)
- Logging de requests en consola (stdout)
- Separación clara entre versiones (labels y selectors)
- Simulación realista de tráfico
- Scripts reutilizables y estructurados

---

## 📄 Licencia

MIT © [Tu nombre]
