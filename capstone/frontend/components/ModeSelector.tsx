interface Props {
  mode: string;
  setMode: (value: string) => void;
}

export default function ModeSelector({ mode, setMode }: Props) {
  return (
    <select
      value={mode}
      onChange={(e) => setMode(e.target.value)}
      className="p-2 border rounded-lg w-full"
    >
      <option value="academic">Academic Assistance</option>
      <option value="placement">Placement AI</option>
      <option value="research">Research Paper Explainer</option>
      <option value="debug">Coding Debug Assistant</option>
      <option value="startup">Startup Idea Evaluator</option>
    </select>
  );
}