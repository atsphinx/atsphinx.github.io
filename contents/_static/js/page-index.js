const textPrefix = "Documentation meets ";
const textPattern = ["...", "Presentation", "Demonstration"];
const intervalOptions = {
  typing: 100,
  deleting: 50,
  waitingForType: 1000,
  waitingForDelete: 3000,
};

let currentIndex = 0;

function runType(elm, current, target) {
  current += target[current.length];
  elm.innerHTML = `${textPrefix}${current}`;
  if (current !== target) {
    setTimeout(() => runType(elm, current, target), intervalOptions.typing);
  } else {
    setTimeout(() => runDelete(elm, current), intervalOptions.waitingForDelete);
  }
}

function runDelete(elm, current) {
  current = current.slice(0, -1);
  elm.innerHTML = `${textPrefix}${current}`;
  if (current !== "") {
    setTimeout(() => runDelete(elm, current), intervalOptions.deleting);
    return;
  }
  currentIndex++;
  if (currentIndex >= textPattern.length) {
    currentIndex = 0;
  }
  const target = textPattern[currentIndex];
  setTimeout(
    () => runType(elm, current, target),
    intervalOptions.waitingForType,
  );
}

function start(selector) {
  const elm = document.querySelector(selector);
  setTimeout(
    () => runDelete(elm, textPattern[currentIndex]),
    intervalOptions.waitingForType,
  );
}

start(".hero p.title");
