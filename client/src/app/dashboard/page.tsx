import { getServerSession } from "next-auth";
import { authOptions } from "../api/auth/[...nextauth]/route";
import { redirect } from "next/navigation";
import LogOutBtn from "@/components/logOutBtn";

export default async function PageDashboard() {
  const session = await getServerSession(authOptions);

  if (!session) {
    redirect("/login");
  }

  return (
    <>
      <h1 className="text-2xl font-bold">Dashboard</h1>
      <div className="flex items-center justify-center h-screen bg-gray-200 p-4 sm:p-6">
        <p>Bienvenido, {session?.user?.name}</p>
        <LogOutBtn />
      </div>
    </>
  );
}